from yandiyacbm.py4dbp import Order, Packer
from yandiyacbm.py4dbp_utils import initiate_pallets, pre_pack, re_pack


def divider():
    print("\n------------------------------------------------------------------------------------------------------------------------")


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

def order_display(order: Order):
    for Packer in order.packers:
        for Bin in Packer.bins:
            #if len(Bin.unfitted_items) == 0:
            print(":::::::::::", Bin.string())
            print("FITTED ITEMS:")
            for item in Bin.items:
                print("====> ", item.string())
