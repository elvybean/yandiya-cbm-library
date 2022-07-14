"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
from yandiyacbm.py4dbp import Order, Packer, Bin, Item


def binpack(formattedData: list):
    order = Order()
    packer = Packer()
    initiate_pallets(packer)
    pre_pack(packer, formattedData)
    packer.pack()
    output = pallet_select(packer)
    order.add_packer(packer)

    while output != False:
        packer2 = Packer()
        initiate_pallets(packer2)
        re_pack(packer2, output)
        packer2.pack()
        order.add_packer(packer2)
        output = pallet_select(packer2)

    if output == False:
        return order


def initiate_pallets(packer: Packer):
    packer.add_bin(Bin("standard-quarter", 1200, 1200, 800, 300))
    packer.add_bin(Bin("standard-half", 1200, 1200, 1200, 600))
    packer.add_bin(Bin("standard", 1200, 1200, 2200, 1200))
    packer.add_bin(Bin("euro-quarter", 800, 1200, 800, 300))
    packer.add_bin(Bin("euro-half", 800, 1200, 1200, 600))
    packer.add_bin(Bin("euro", 800, 1200, 2200, 1200))
    return packer


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
                    Item(details[0], details[1], details[2], details[3], details[4]))
    return packer


def pallet_select(packer: Packer):
    num = 0
    for Bin in packer.bins:
        num += 1
        leftoverItems = []
        if len(Bin.unfitted_items) == 0:
            return False
        elif num == len(packer.bins):
            for item in Bin.unfitted_items:
                leftoverItems.append(item)
            return leftoverItems
