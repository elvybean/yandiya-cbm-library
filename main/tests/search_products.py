"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to test the search_product fucntion
"""

#####################################################################################
#"import cbmcalculator as cbm" should not be up here! if it is move to other comment#
#####################################################################################
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
#####################################################################################
#the line "import cbmcalculator as cbm" ALWAYS needs to be below the above lines ####
import cbmcalculator as cbm #########################################################
#####################################################################################

def main():
    f = open("main/tests/tests.txt", "r")
    print(f.read())
    f.close()

    parameters = input(
        "\nWhats the product number, barcode or sku of the item?  ")
    productQuantity = int(input(
        "\nWhat's the quantity of the items that you need?  "))

    inWarehouse = cbm.search_product(parameters)

    if inWarehouse == 0:
        print("\nerror. either incorrect input or item does not exist  ")
    else:
        print(inWarehouse)

    response = input(
        "\nDo you want to test function again? y/n  ").capitalize()

    if response == "N":
            return 0
    else:
        return main()

main()