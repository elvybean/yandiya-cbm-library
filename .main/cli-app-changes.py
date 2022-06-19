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


def testFunc():
    IterateStore = [0, 0]  # List that contains 2 integers;
    # the first int stores the cbm & the second int stores the weight
    ErrorDetect = [0, 0]  # List that contains 2 integers;
    # the first int counts the errors & the second int counts the number of iterations

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

    input("\nDo you want to search for another item? y/n  ")
    if input == "Y" or input == "y" or input == "Yes" or input == "yes":
        testFunc()

    elif input == "N" or input == "n" or input == "No" or input == "no":
        if ErrorDetect[1] == ErrorDetect[0]:
            return 0

        else:
            return IterateStore

    else:
        testFunc()
        print("else")


def main():
    cbm = testFunc()

    if cbm != 0:
        print("The Total  CBM is ", cbm[0], ", the total weight is ",
              cbm[1])
        # " the items will be sent in a ", cbm[2]) #fix parcel or package logic

    else:
        print("There are no values to output")


main()
