"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to interact 
with the yandiya-cbm-library.

CHANGED untest versions of cli-app
file was created as cli-app needed to be rolled back in order to test chnanges of cbmcalculator
"""
import cbmcalculator


def testFunc(IterateStore: list, ErrorDetect: list):
    parameters = input(
        "\n\nWhats the product number, barcode or sku of the item? ")
    productQuantity = int(input(
        "\nWhat's the quantity of the items that you need? "))

    inWarehouse = cbmcalculator.searching_product(parameters)

    if inWarehouse == 0:
        print("error. either incorrect input or item does not exist")
        ErrorDetect[0] += 1

    else:
        # print("\n\n", inWarehouse, "\n\n")
        cbm = cbmcalculator.calculate(inWarehouse, productQuantity)

        IterateStore[0] += cbm[0]
        IterateStore[1] += cbm[1]

    input("Do you want to search for another item? y/n").capitalize()
    if input == "Y":
        ErrorDetect[1] += 1
        testFunc()

    elif input == "N":
        if ErrorDetect[1] == ErrorDetect[0]:
            return 0
        else:
            return IterateStore

    else:
        ErrorDetect[1] += 1
        testFunc()


cbm = testFunc(list, list)

if cbm != 0:
    print("The Total  CBM is ", cbm[0], ", the total weight is ",
          cbm[1])
    # " the items will be sent in a ", cbm[2]) #fix parcel or package logic

else:
    print("There are no values to output")
