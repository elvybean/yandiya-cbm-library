from yandiyacbm.packer import Packer

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
            