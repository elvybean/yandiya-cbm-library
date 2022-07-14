from yandiyacbm.py4dbp import Order, Packer
from yandiyacbm.py4dbp_utils import initiate_pallets, pre_pack, re_pack


def divider():
    print("")
    print("------------------------------------------------------------------------------------------------------------------------")


def parameters_display(formattedData: list):
    divider()
    print("\nFormtted Data")
    for i in range(len(formattedData)):
        item = formattedData[i]
        for j in range(len(item)):
            if j == 0:
                print("\n:::::::::::", item[j])
            else:
                print("====> ", item[j])
    divider()


def binpack_prints(formattedData: list):
    packer = Packer()
    initiate_pallets(packer)
    pre_pack(packer, formattedData)
    packer.pack()
    output = pallet_select_prints(packer)
    divider()

    while output != False:
        packer2 = Packer()
        initiate_pallets(packer2)
        re_pack(packer2, output)
        packer2.pack()
        output = pallet_select_prints(packer2)
        divider()
    if output == False:
        return


def pallet_select_prints(packer: Packer):
    num = 0
    for Bin in packer.bins:
        num += 1
        leftoverItems = []

        if len(Bin.unfitted_items) == 0:
            print("\nAppropriate bin found\n")
            print(":::::::::::", Bin.string())
            print("FITTED ITEMS:")
            for item in Bin.items:
                print("====> ", item.string())
            return False

        elif num == len(packer.bins):
            print("\nClosest bin found\n")
            print(":::::::::::", Bin.string())
            print("FITTED ITEMS:")
            for item in Bin.items:
                print("====> ", item.string())
            print("UNFITTED ITEMS:")
            for item in Bin.unfitted_items:
                leftoverItems.append(item)
                print("====> ", item.string())
            return leftoverItems


def order_output(order: Order):
    for Packer in order.packers:
        for Bin in Packer.bins:
            if len(Bin.unfitted_items) == 0:
                print(":::::::::::", Bin.string())
                print("FITTED ITEMS:")
                for item in Bin.items:
                    print("====> ", item.string())
