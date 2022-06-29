"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is CLI python application designed to test the shipping_logic fucntion
"""
import cbmcalculator


def main():
    f = open(".main\welcome2.txt", "r")
    print(f.read())
    f.close()

    cbm = float(input(
        "\nWhats the product's CBM?  "))
    productQuantity = float(input(
        "\nWhat's the product's weight?  "))

    out = cbmcalculator.shipping_logic(cbm, productQuantity)

    print(out)

    response = input(
        "\nDo you want to test function again? y/n  ").capitalize()

    if response == "N":
        return 0
    else:
        return main()


main()
