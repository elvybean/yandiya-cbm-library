"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to test the search_product fucntion
"""

#######################################################################################
#import yandiyacbm as yandiya should not be up here! if it is move to other comment ###
#######################################################################################
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
#######################################################################################
#import yandiyacbm as yandiya ALWAYS needs to be below import os and import sys #######
#######################################################################################
from yandiyacbm import search_product #################################################s
#######################################################################################
from tests import startup

def main():
    
    startup()
    
    parameters = input(
        "\nWhats the product number, barcode or sku of the item?  ")
    productQuantity = int(input(
        "\nWhat's the quantity of the items that you need?  "))

    inWarehouse = search_product(parameters)

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