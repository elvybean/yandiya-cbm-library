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
################################################################################
#the line "yandiyacbm as yandiya" ALWAYS needs to be below os and sys imports ##
import yandiyacbm as yandiya ###################################################
################################################################################


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

    extractedRows = []
    errorDetect = [0, 0]
    repeat = "Yes"

    while repeat != "N":
        errorDetect[1] += 1

        parameters = input(
            "\nWhats the product number, barcode or sku of the item?  ")
        productQuantity = int(input(
            "\nWhat's the quantity of the items that you need?  "))

        productrow = yandiya.search_product(parameters)

        if productrow == 0:
            errorDetect[0] += 1
            print("\nerror. either incorrect input or item does not exist  ")
        else:
            extractedRows.append([productrow, productQuantity])

        repeat = input(
            "\nDo you want to search for another item? y/n  ").capitalize()

        if repeat == "N":
            break

    if extractedRows == []:
        print("\nerror.")
        return 0

    binpackParams = []

    for i in range(len(extractedRows)):
        j = extractedRows[i]
        
        k = yandiya.parameters(j[0], j[1])
        binpackParams.append(k)

    for n in range(len(binpackParams)):
        #for o in range(len(binpackParams[n])):
            #print(binpackParams[n][o])
        print(binpackParams[n])


main()
