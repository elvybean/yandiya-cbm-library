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


def re_pack(packer: Packer, unfitted: list):
    for item in unfitted:
        packer.add_item(item)
    return packer


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


def pallet_select(packer: Packer):
    num = 0
    for Bin in packer.bins:
        num += 1
        leftoverItems = []
        if len(Bin.unfitted_items) == 0:
            return [False, Bin]
        elif num == len(packer.bins):
            for item in Bin.unfitted_items:
                leftoverItems.append(item)
            return [leftoverItems, Bin]


def pallet_purge(packer: Packer, choosen_bin: Bin):
    for Bin in packer.bins:
        if Bin.name != choosen_bin.name and packer.total_bins != 1:
            packer.remove_bin(Bin)
    return packer
    # problem: due to pallets' Bin Object names starting with either 'euro' or 'standard' 
    # pallet_purge() only 'purges' half of pallets from packer not all but 1
    # problem (2): created bin_def value in Bin class and used it to compare the 
    # iterated 'Bin' object in pallet_purge() and the 'choosen_bin' object but the 
    # same issue persists as only half of the pallets are purged


def initiate_pallets(packer: Packer):
    packer.add_bin(Pallets.standard_quarter)
    packer.add_bin(Pallets.standard_half)
    packer.add_bin(Pallets.standard)
    packer.add_bin(Pallets.euro_quarter)
    packer.add_bin(Pallets.euro_half)
    packer.add_bin(Pallets.euro)
    return packer
