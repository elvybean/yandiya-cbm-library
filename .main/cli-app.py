"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to interact 
with the yandiya-cbm-library

"""
import cbmcalculator

parameters = input("Whats the product number, barcode or sku of the item? ")
productQuantity = int(input(
    "\nWhat's the quantity of the items that you need? "))

inWarehouse = cbmcalculator.searching_product(parameters)
if inWarehouse == 0:
    print("error. either incorrect input or item does not exist")
else:
    cbm = cbmcalculator.calculate(inWarehouse, productQuantity)

    sentWith = cbmcalculator.weight_logic(cbm[1])

    print("The CBM is ", cbm[0], ", the total weight is ",
          cbm[1], " the items will be sent in a ", sentWith)
