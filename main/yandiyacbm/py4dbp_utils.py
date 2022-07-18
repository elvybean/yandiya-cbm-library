"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
from yandiyacbm.py4dbp import Order, Packer, Bin, Item
from yandiyacbm.py4dbp_pallets import Pallets


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
    else:  # error handling
        return False


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
            return False
        elif num == len(packer.bins):
            for item in Bin.unfitted_items:
                leftoverItems.append(item)
            return leftoverItems


def initiate_pallets(packer: Packer):
    packer.add_bin(Pallets.standard_quarter)
    packer.add_bin(Pallets.standard_half)
    packer.add_bin(Pallets.standard)
    packer.add_bin(Pallets.euro_quarter)
    packer.add_bin(Pallets.euro_half)
    packer.add_bin(Pallets.euro)
    return packer
