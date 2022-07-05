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
import cbmcalculator as cbm #########################################################
#####################################################################################


def listCreate(iterateStore: list, ErrorDetect: list):
    """Creates a list that contains the extacted excel rows of selected products + item quantities

    Args:
        IterateStore (list): (is orginally empty when called from main) stores the extacted excel rows of selected products 
            + item quantities in a 2 Dimensional list
        ErrorDetect (list): list of integer; the first int counts the errors & the second int counts the number of iterations

    Returns:
        IterateStore (list): stores the extacted excel rows of selected products + item quantities in a 2 Dimensional list
    """

    ErrorDetect[1] += 1

    parameters = input(
        "\nWhats the product number, barcode or sku of the item?  ")
    productQuantity = int(input(
        "\nWhat's the quantity of the items that you need?  "))

    inWarehouse = cbm.search_product(parameters)

    if inWarehouse == 0:
        ErrorDetect[0] += 1
        print("\nerror. either incorrect input or item does not exist  ")
    else:
        iterateStore.append([inWarehouse, productQuantity])

    response = input(
        "\nDo you want to search for another item? y/n  ").capitalize()

    if response == "N":
        if not ErrorDetect[0] > ErrorDetect[1]:
            return iterateStore 
        else:
            return 0
    else:
        return listCreate(iterateStore, ErrorDetect)


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

    listParameter = listCreate([], [0, 0])

    multipleCBM = cbm.main(listParameter)

    # tabulate table?? + pandas??
    #print("The Total  CBM is ", multipleCBM[0], ", the total weight is ", multipleCBM[1], " the items will be sent in a ", multipleCBM[2])
    print(multipleCBM)

    

main()