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


def re_pack():
    #needs to 're_pack' the unfitted item objects - will take the input as a list
    return 0


def unfit_items():
    #needs to 'package' Bin.unfitted_items into a list to be repacked
    return 0


def bin_purge():
    #needs to remove all bins but the bin of best fit
    return 0


def initiate_pallets(packer: Packer):
    packer.add_bin(Pallets.standard_quarter)
    packer.add_bin(Pallets.standard_half)
    packer.add_bin(Pallets.standard)
    packer.add_bin(Pallets.euro_quarter)
    packer.add_bin(Pallets.euro_half)
    packer.add_bin(Pallets.euro)
    return packer
