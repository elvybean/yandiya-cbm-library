"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

This is a CLI python application designed to interact with the yandiyacbm library.
"""
#######################################################################################
#import yandiyacbm as yandiya should not be up here! if it is move to other comment ###
#######################################################################################
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
#######################################################################################
#import yandiyacbm ALWAYS needs to be below import os and import sys ##################
#######################################################################################
from yandiyacbm import search_product, parameter_generate, Packer, Bin, Item, pallet_select, pre_pack, initiate_pallets, re_pack
#######################################################################################


def divider():
    e = open("main/cli-app/divider.txt", "r")
    print("\n", e.read())
    e.close()


def userInput(iterate: list, errors: list):
    errors[1] += 1

    parameters = input(
        "\nWhats the product number, barcode or sku of the item?  ")
    productQuantity = int(input(
        "\nWhat's the quantity of the items that you need?  "))

    productrow = search_product(parameters)

    if productrow == 0:
        errors[0] += 1
        print("\nerror. either incorrect input or item does not exist  ")
    else:
        iterate.append([productrow, productQuantity])

    repeat = input(
        "\nDo you want to search for another item? y/n  ").capitalize()

    if repeat == "N":
        if not errors[0] > errors[1]:
            return iterate
        else:
            return 0
    else:
        return userInput(iterate, errors)


def generate(params: list):
    iterate = []

    for i in range(len(params)):
        product = params[i]
        formatted = parameter_generate(product[0], product[1])
        iterate.append(formatted)

    return iterate


def display(params: list):
    divider()
    print("\nFormtted Data")
    for i in range(len(params)):
        item = params[i]
        for j in range(len(item)):
            if j == 0:
                print("\n:::::::::::", item[j])
            else:
                print("====> ", item[j])
    divider()
    return


def main():

    # this is unnecessary but cool
    e = open("main/cli-app/cli-app.txt", "r")
    print(e.read())
    e.close()

    try:
        extractedRows = userInput([], [0, 0])
    except:
        print("\nerror. something went wrong")

    try:
        params = generate(extractedRows)
    except:
        print("\nerror. something went wrong")

    try:
        display(params)
    except:
        print("\nerror. something went wrong")

    try:
        packer = Packer()
        initiate_pallets(packer)
        pre_pack(packer, params)
        packer.pack()
        output = pallet_select(packer)
        divider()
        if output == False:
            return

    except:
        print("\nerror. something went wrong")

    try:
        packer2 = Packer()
        initiate_pallets(packer2)
        re_pack(packer2, output)
        packer2.pack()
        pallet_select(packer2)
        divider()

    except:
        print("\nerror. something went wrong")


if __name__ == "__main__":
    main()
