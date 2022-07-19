"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
from yandiyacbm.py4dbp import Order, Packer, Bin, Item


class Pallets:
    standard_quarter = Bin("standard-quarter", 1200, 1200, 800, 300)
    standard_half = Bin("standard-half", 1200, 1200, 1200, 600)
    standard = Bin("standard", 1200, 1200, 2200, 1200)
    euro_quarter = Bin("euro-quarter", 800, 1200, 800, 300)
    euro_half = Bin("euro-half", 800, 1200, 1200, 600)
    euro = Bin("euro", 800, 1200, 2200, 1200)


def pre_pack(packer: Packer, params: list):
    for i in range(len(params)):
        items = params[i]
        for j in range(len(items)):
            if j != 0:
                details = items[j]
                packer.add_item(
                    Item(details[0], details[1],
                         details[2], details[3], details[4])
                )
    return packer


def re_pack(newPacker: Packer, oldPacker: Packer):
    for item in oldPacker.unfit_items:
        newPacker.add_item(item)
    return newPacker


"""
def re_pack(packer: Packer, unfitted: list):
    for item in unfitted:
        packer.add_item(item)
    return packer

def unfit_items(packer: Packer):
    iterate = 0
    for Bin in packer.bins:
        iterate += 1
        if len(Bin.unfitted_items) == 0: #finds the first bin that fits
            return False
        if iterate == len(packer.bins): #finds the bin of best fit (the last one)
            leftoverItems = []
            for item in Bin.unfitted_items:
                leftoverItems.append(item)
            return leftoverItems
"""

"""
# ^ comment out the above line to use the 
# better versions of functions which will be fixed and 
# used instead of the placeholders below this DocString

def unfit_items(packer: Packer):
    if len(packer.unfit_items) != 0:
        return False #returns False because all items are not fitted
    else:
        return True # returns True because all items are fitted

def bin_purge(packer: Packer):
    print(len(packer.unfit_items)) #testing
    print(len(packer.bins)) #testing
    if len(packer.unfit_items) != 0:
        i = 0
        for Bin in packer.bins:
            i += 1
            print("i  is: ", i) #testing
            if i != len(packer.bins):
                print("if i != len(packer.bins) called") #testing
                packer.remove_bin(Bin)
    else: #if len(packer.unfit_items) == 0
        j = 0
        for Bin in packer.bins:
            j += 1
            if j != 1: 
                print("if j != 1: called") #testing
                packer.remove_bin(Bin)
    return packer

"""


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

# """


def initiate_pallets(packer: Packer):
    packer.add_bin(Pallets.standard_quarter)
    packer.add_bin(Pallets.standard_half)
    packer.add_bin(Pallets.standard)
    packer.add_bin(Pallets.euro_quarter)
    packer.add_bin(Pallets.euro_half)
    packer.add_bin(Pallets.euro)
    return packer
