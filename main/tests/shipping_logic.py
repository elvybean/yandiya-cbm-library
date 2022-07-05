"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to test the shipping_logic fucntion
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


def main():
    f = open("main/tests/tests.txt", "r")
    print(f.read())
    f.close()

    cbm = float(input(
        "\nWhats the product's CBM?  "))
    productQuantity = float(input(
        "\nWhat's the product's weight?  "))

    out = cbm.shipping_logic(cbm, productQuantity)

    print(out)

    response = input(
        "\nDo you want to test function again? y/n  ").capitalize()

    if response == "N":
        return 0
    else:
        return main()


main()