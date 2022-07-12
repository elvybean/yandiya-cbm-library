"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to test the fucntions in the excel_func module
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
from yandiyacbm import search_product, parameter_generate #############################
#######################################################################################
from tests import startup

def main():
    
    print(startup())
    
    search = input(
        "\nWhats the product number, barcode or sku of the item?  ")
    quant = int(input(
        "\nWhat's the quantity of the items that you need?  "))

    row = search_product(search)

    if row == 0:
        print("\nerror. either incorrect input or item does not exist  ")
    else:
        out = parameter_generate(row, quant)
        
        for i in range(len(out)):
            if i == 0:
                 print(":::::::::::", out[i])
            else:
                print("====> ",out[i])


    response = input(
        "\nDo you want to test function again? y/n  ").capitalize()

    if response == "N":
            return 0
    else:
        return main()

if __name__ == "__main__":
   main()