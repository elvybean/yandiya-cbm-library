from yandiyacbm.py4dbp import Packer, Item

def pre_pack(packer: Packer, params: list):
    for i in range(len(params)):
        items = params[i]
        for j in range(len(items)):
            if j != 0:
                details = items[j]
                name = str(details[0])
                width = float(details[1])
                height = float(details[2])
                depth = float(details[3])
                weight = float(details[4])
                packer.add_item(Item(name, width, height, depth, weight))
                #Item(details[0], details[1], details[2], details[3], details[4])

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
            