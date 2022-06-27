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
        cbm = [0, 0]
        print("\nerror. either incorrect input or item does not exist  ")

    else:
        cbm = cbmcalculator.calculate(inWarehouse, productQuantity)

    for i in range(len(cbm)):
        IterateStore[i] += cbm[i]

    print(cbm)  # for testing purposes
    print(IterateStore)  # for testing purposes

    response = input(
        "\nDo you want to search for another item? y/n  ").capitalize()

    if response == "N":
        return IterateStore

    else:
        testFunc(IterateStore, ErrorDetect)


def main():
    """holds the main code of this py file
    Args: 
        none

    Returns: 
        none
    """

    print(testFunc([0, 0], [0, 0]))


main()
