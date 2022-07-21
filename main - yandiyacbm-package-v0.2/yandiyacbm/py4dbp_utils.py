from yandiyacbm.py4dbp import Packer, Item

def pre_pack(packer: Packer, formattedData: list):
    for i in range(len(formattedData)):
        product = formattedData[i]
        for j in range(len(product)):
            if j != 0:
                details = product[j]
                packer.add_item(
                    Item(details[0], details[1],
                         details[2], details[3], details[4])
                )
    return packer


def select(packer: Packer):
    for Bin in packer.bins:
        if len(Bin.unfitted_items) == 0:
            print("Appropriate bin found\n")

            print(":::::::::::", Bin.string())

            print("FITTED ITEMS:")
            for item in Bin.items:
                print("====> ", item.string())
            return

def orginal(packer: Packer):
    for Bin in packer.bins:
        print(":::::::::::", Bin.string())

        print("FITTED ITEMS:")
        for item in Bin.items:
            print("====> ", item.string())

        print("UNFITTED ITEMS:")
        for item in Bin.unfitted_items:
            print("====> ", item.string())
            