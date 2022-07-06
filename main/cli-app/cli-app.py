"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to interact with the yandiya-cbm-library.
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
import cbmcalculator as cbmcalc #########################################################
#####################################################################################

def main():
    """holds the main code of this py file
    Args:
        none

    Returns:
        none
    """

    # this is unnecessary but cool
    f = open("main/cli-app/cli-app.txt", "r")
    print(f.read())
    f.close()

    listParameter = []
    ErrorDetect = [0, 0]
    response = ""

    while response != "N":
        ErrorDetect[1] += 1

        parameters = input(
            "\nWhats the product number, barcode or sku of the item?  ")
        productQuantity = int(input(
            "\nWhat's the quantity of the items that you need?  "))

        inWarehouse = cbmcalc.search_product(parameters)

        if inWarehouse == 0:
            ErrorDetect[0] += 1
            print("\nerror. either incorrect input or item does not exist  ")
        else:
            listParameter.append([inWarehouse, productQuantity])

        response = input(
            "\nDo you want to search for another item? y/n  ").capitalize()

        if response == "N":
            break

    if listParameter == []:
        print("\nerror.")
        return 0

    cbm = 0
    weight = 0
    binpackParams= []

    for i in range(len(listParameter)):
        j = listParameter[i]
        k = cbmcalc.calculate(j[0], j[1])
        cbm += k[0]
        weight += k[1]
        binpackParams.append([k[2],k[3]])

    shipping = cbmcalc.bin_packing(cbm, weight, binpackParams)

    print(cbm, weight, binpackParams, shipping)

main()
