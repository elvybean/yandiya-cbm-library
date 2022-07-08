"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

This is a CLI python application designed to interact with the yandiyacbm library.
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
from yandiyacbm import search_product, parameters, shipping_approx, extract ###########
#######################################################################################

def startup(): # this is unnecessary but cool
    e = open("main/cli-app/cli-app.txt", "r")
    value = (e.read())
    e.close()
    return value


def userInput(iterate: list, errors: list):
    errors[1] += 1

    parameters = input(
        "\nWhats the product number, barcode or sku of the item?  ")
    productQuantity = int(input(
        "\nWhat's the quantity of the items that you need?  "))


    productrow = search_product(parameters)

    if productrow == 0:
        errors[0] += 1
        print("\nerror. either incorrect input or item does not exist  ")
    else:
        iterate.append([productrow, productQuantity])

    repeat = input(
        "\nDo you want to search for another item? y/n  ").capitalize()

    if repeat == "N":
        if not errors[0] > errors[1]:
            return iterate
        else:
            return 0
    else:
        return userInput(iterate, errors)

def generate(params: list):
    iterate = []

    for l in range(len(params)):
        v = params[l]
        
        i = parameters(v[0], v[1])
        iterate.append(i)

    return iterate

def display(params: list):
    for s in range(len(params)):
        print(params[s])
        print(shipping_approx(extract(params[s])))
        print("==========")

def main():

    try:
        print(startup())
    except:
        print("\nerror. something went wrong")

    try:
        extractedRows = userInput([], [0, 0])
    except:
        print("\nerror. something went wrong")

    try:
        binpackInput = generate(extractedRows)
    except:
        print("\nerror. something went wrong")

    try:
        display(binpackInput)
    except:
        print("\nerror. something went wrong")



main()
