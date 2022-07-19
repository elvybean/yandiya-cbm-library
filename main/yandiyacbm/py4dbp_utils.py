"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
from yandiyacbm.py4dbp import Packer, Bin, Item


class Pallets:
    standard_quarter = Bin("standard-quarter", 1200, 1200, 800, 300)
    standard_half = Bin("standard-half", 1200, 1200, 1200, 600)
    standard = Bin("standard", 1200, 1200, 2200, 1200)
    euro_quarter = Bin("euro-quarter", 800, 1200, 800, 300)
    euro_half = Bin("euro-half", 800, 1200, 1200, 600)
    euro = Bin("euro", 800, 1200, 2200, 1200)


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


def re_pack(packer: Packer, unfitted: list):
    #needs to 're_pack' the unfitted item objects - will take the input as a list
    for item in unfitted:
        packer.add_item(item)
    return packer


def unfit_items(packer: Packer):
    #needs to 'package' Bin.unfitted_items into a list to be repacked
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


def initiate_pallets(packer: Packer):
    packer.add_bin(Pallets.standard_quarter)
    packer.add_bin(Pallets.standard_half)
    packer.add_bin(Pallets.standard)
    packer.add_bin(Pallets.euro_quarter)
    packer.add_bin(Pallets.euro_half)
    packer.add_bin(Pallets.euro)
    return packer
