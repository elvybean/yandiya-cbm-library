from yandiyacbm.py4dbp import Packer

# old list based versions


def re_pack(packer: Packer, unfitted: list):
    for item in unfitted:
        packer.add_item(item)
    return packer


def unfit_items(packer: Packer):
    iterate = 0
    for Bin in packer.bins:
        iterate += 1
        if len(Bin.unfitted_items) == 0:  # finds the first bin that fits
            return False
        if iterate == len(packer.bins):  # finds the bin of best fit (the last one)
            unfitted = []
            for item in Bin.unfitted_items:
                unfitted.append(item)
            return unfitted


# better versions of functions which will be fixed and
# used instead of the placeholders below this DocString

def unfit_items(packer: Packer):
    if len(packer.unfit_items) != 0:
        return False  # returns False because all items are not fitted
    else:
        return True  # returns True because all items are fitted


def bin_purge(packer: Packer):
    print(len(packer.unfit_items))  # testing
    print(len(packer.bins))  # testing
    if len(packer.unfit_items) != 0:
        i = 0
        for Bin in packer.bins:
            i += 1
            print("i  is: ", i)  # testing
            if i != len(packer.bins):
                print("if i != len(packer.bins) called")  # testing
                packer.remove_bin(Bin)
    else:  # if len(packer.unfit_items) == 0
        j = 0
        for Bin in packer.bins:
            j += 1
            if j != 1:
                print("if j != 1: called")  # testing
                packer.remove_bin(Bin)
    return packer


# (Was) Currently Used

def re_pack(newPacker: Packer, oldPacker: Packer):
    for item in oldPacker.unfit_items:
        newPacker.add_item(item)
    return newPacker


def unfit_items(packer: Packer):
    for Bin in packer.bins:
        if len(Bin.unfitted_items) != 0:
            return False  # returns False because all items are not fitted
        else:
            return True  # returns True because all items are fitted


def bin_purge(packer: Packer):
    newPacker = Packer()
    iterate = 0
    for Bin in packer.bins:
        iterate += 1
        if len(Bin.unfitted_items) == 0:  # finds the first bin that fits
            newPacker.add_bin(Bin)
            return newPacker
        if iterate == len(packer.bins):  # finds the bin of best fit (the last one)
            newPacker.add_bin(Bin)
            return newPacker
