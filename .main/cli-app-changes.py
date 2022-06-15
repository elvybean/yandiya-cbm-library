"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to interact 
with the yandiya-cbm-library.

CHANGED untest versions of cli-app
file was created as cli-app needed to be rolled back in order to test chnanges of cbmcalculator
Script has ERRORS
"""
import cbmcalculator


cbmStore = []
search = True
while search == True:
    parameters = input(
        "\n\nWhats the product number, barcode or sku of the item? ")
    productQuantity = int(input(
        "\nWhat's the quantity of the items that you need? "))

    inWarehouse = cbmcalculator.searching_product(parameters)

    if inWarehouse == 0:
        print("error. either incorrect input or item does not exist")

    else:
        print("\n\n", inWarehouse, "\n\n")
        cbm = cbmcalculator.calculate(inWarehouse, productQuantity)

    input("Do you want to search for another item? y/n").capitalize()
    if input == "Y" and inWarehouse != 0:
        cbmStore[0] = cbm[0]
        cbmStore[1] = cbm[1]

    elif input == "N":
        search = False
        # while loop not working using break as temporary fix
        break

    else:
        search = True

print("The Total  CBM is ", cbmStore[0], ", the total weight is ",
      cbmStore[1])

# " the items will be sent in a ", cbmStore[2]) #fix parcel or package logic
