"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to interact 
with the yandiya-cbm-library.

Adding calculate cbm of multiple items
"""
import cbmcalculator


def testFunc(IterateStore: list, ErrorDetect: list):
    """Holds the main logic that accesses the cbmcalculator library

    Args:
        IterateStore (list): list of ints; the first int stores the cbm & the second int stores the weight
        ErrorDetect (list): list of ints; the first int counts the errors & the second int counts the number of iterations

    Returns:
        list: stores the calculated cbm and the total weight OR 0 values
    """

    ErrorDetect[1] += 1

    parameters = input(
        "\n\nWhats the product number, barcode or sku of the item?  ")
    productQuantity = int(input(
        "\nWhat's the quantity of the items that you need?  "))

    inWarehouse = cbmcalculator.searching_product(parameters)
    if inWarehouse == 0:
        ErrorDetect[0] += 1
        print("\nerror. either incorrect input or item does not exist  ")

    else:
        cbm = cbmcalculator.calculate(inWarehouse, productQuantity)

        IterateStore[0] += cbm[0]
        IterateStore[1] += cbm[1]

    response = input(
        "\nDo you want to search for another item? y/n  ").capitalize()
    if response == "Y" or response == "Yes":
        if ErrorDetect[1] == ErrorDetect[0]:
            testFunc([0, 0], ErrorDetect)
        else:
            testFunc(IterateStore, ErrorDetect)

    elif response == "N" or response == "No":
        if ErrorDetect[1] == ErrorDetect[0]:
            return [0, 0]
        else:
            return [IterateStore[0], IterateStore[1]]

    else:
        testFunc(IterateStore, ErrorDetect)


def main():
    """holds the main code of the py file
    Args: 
        none

    Returns: 
        none
    """
    emptyList = [0, 0]
    cbm = testFunc(emptyList, emptyList)

    print(cbm)


main()
