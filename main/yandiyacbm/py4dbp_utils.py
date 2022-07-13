"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
from yandiyacbm.py4dbp import Packer, Item


def pre_pack(packer: Packer, params: list):
    for i in range(len(params)):
        items = params[i]
        for j in range(len(items)):
            if j != 0:
                details = items[j]
                packer.add_item(
                    Item(details[0], details[1], details[2], details[3], details[4]))
    return packer


def select(packer: Packer):
    num = 0
    for Bin in packer.bins:
        num += 1
        if len(Bin.unfitted_items) == 0:
            print("Appropriate bin found\n")

            print(":::::::::::", Bin.string())

            print("FITTED ITEMS:")
            for item in Bin.items:
                print("====> ", item.string())
            return

        elif num == len(packer.bins):
            print("Closest bin found\n")
            print(":::::::::::", Bin.string())

            print("FITTED ITEMS:")
            for item in Bin.items:
                print("====> ", item.string())

            print("UNFITTED ITEMS:")
            for item in Bin.unfitted_items:
                print("====> ", item.string())
            return
