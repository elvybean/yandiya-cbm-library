"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

This is a CLI python application designed to interact with the yandiyacbm library.
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
from yandiyacbm import search_products, parameters_generate, parameters_display, binpack_start_prints


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

    extractedRows = cliapp_Input([], [0, 0])

    params = parameters_generate(extractedRows)

    parameters_display(params)

    binpack_start_prints(params)

if __name__ == "__main__":
    main()
