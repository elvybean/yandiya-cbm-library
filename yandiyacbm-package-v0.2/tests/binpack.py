"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to test the functions & classes in the binpack module
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
#import yandiyacbm ALWAYS needs to be below import os and import sys ##################
#######################################################################################
from yandiyacbm import Packer, Bin, Item, select, orginal #############################
#######################################################################################
from tests import startup

def main():
    print(startup())

    packer = Packer()

    # Formatted values based on yandiyacbm
    # ['IH35-W', [2.0, 0.04422, 9.56, 670.0, 660.0, 50.0, 4.78], [2.0, 0.2485, 51.84, 700.0, 710.0, 250.0, 25.92]]
    # Output according to yandiyacbm
    # ['euro-quarter', 1]

    packer.add_bin(Bin("standard-quarter", 1200, 1200, 800, 300))
    packer.add_bin(Bin("standard-half", 1200, 1200, 1200, 600))
    packer.add_bin(Bin("standard", 1200, 1200, 2200, 1200))
    packer.add_bin(Bin("euro-quarter", 800, 1200, 800, 300))
    packer.add_bin(Bin("euro-half", 800, 1200, 1200, 600))
    packer.add_bin(Bin("euro", 800, 1200, 2200, 1200))

    #packer.add_item(Item('Test', 700.0, 710.0, 250.0, 1200.00))
    packer.add_item(Item('IH35-W Outer Carton', 700.0, 710.0, 250.0, 25.92))
    packer.add_item(Item('IH35-W Outer Carton', 700.0, 710.0, 250.0, 25.92))
    packer.add_item(Item('IH35-W Inner Carton', 670.0, 660.0, 50.0, 4.78))
    packer.add_item(Item('IH35-W Inner Carton', 670.0, 660.0, 50.0, 4.78))


    packer.pack()
    #orginal(packer)
    select(packer)

    #print("UNFITTED ITEMS:")
    #for item in b.unfitted_items:
    #    print("====> ", item.string())

    response = input(
        "\nDo you want to test function again? y/n  ").capitalize()

    if response == "N":
            return 0
    else:
        return main()

if __name__ == "__main__":
   main()