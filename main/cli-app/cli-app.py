"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function
"""
#######################################################################################
#import yandiyacbm as yandiya should not be up here! if it is move to other comment
#######################################################################################
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
#######################################################################################
#import yandiyacbm as yandiya ALWAYS needs to be below import os and import sys
#######################################################################################
from yandiyacbm import search_products, multiple_row_format, excelrows_display, formattedData_display, Order, Packer, initiate_pallets, pre_pack, bin_purge, unfit_items, re_pack, order_display

def cliapp_iterate(order: Order, list: list):
    packer = Packer()
    initiate_pallets(packer)

    packer = re_pack(packer, packer) | packer = pre_pack(packer, list)
    packer.pack()

    packer = bin_purge(packer)
    order.add_packer(packer)

    if unfit_items(packer) == False:
        return cliapp_iterate(order, list)
    else:
        return order

def cliapp_Input(iterate: list, errors: list):
    errors[1] += 1

    parameters = input(
        "\nWhats the product number, barcode or sku of the item?  ")
    productQuantity = int(input(
        "\nWhat's the quantity of the items that you need?  "))

    productrow = search_products(parameters)
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
        return cliapp_Input(iterate, errors)


def main():

    # this is unnecessary but cool
    e = open("main/cli-app/cli-app.txt", "r")
    print(e.read())
    e.close()

    extractedRows = cliapp_Input([], [0, 0]) #cli-app func
    if extractedRows == [] or extractedRows == 0:
        return 0
    excelrows_display(extractedRows)

    formattedData = multiple_row_format(extractedRows)
    formattedData_display(formattedData)

    order = Order()

    order = cliapp_iterate(order, formattedData) # cli-app func

    order_display(order)

if __name__ == "__main__":
    main()
