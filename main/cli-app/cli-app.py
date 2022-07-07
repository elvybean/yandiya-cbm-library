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
#import yandiyacbm as yandiya ALWAYS needs to be below import os and import sys #######
#######################################################################################
import yandiyacbm as yandiya ##########################################################
#######################################################################################

def startup(): # this is unnecessary but cool
    f = open("main/cli-app/cli-app.txt", "r")
    value = (f.read())
    f.close()
    return value


def userInput(iterateStore: list, errorDetect: list):
    errorDetect[1] += 1

    parameters = input(
        "\nWhats the product number, barcode or sku of the item?  ")
    productQuantity = int(input(
        "\nWhat's the quantity of the items that you need?  "))

    productrow = yandiya.search_product(parameters)

    if productrow == 0:
        errorDetect[0] += 1
        print("\nerror. either incorrect input or item does not exist  ")
    else:
        iterateStore.append([productrow, productQuantity])

    repeat = input(
        "\nDo you want to search for another item? y/n  ").capitalize()

    if repeat == "N":
        if not errorDetect[0] > errorDetect[1]:
            return iterateStore
        else:
            return 0
    else:
        return userInput(iterateStore, errorDetect)

def initiateParams(params: list):
    iterateStore = []

    for i in range(len(params)):
        j = params[i]
        
        k = yandiya.parameters(j[0], j[1])
        iterateStore.append(k)

    return iterateStore

def displaySelectedRows(params: list):
    for n in range(len(params)):
        print(params[n])
        print(yandiya.shipping(params[n]))

def main():

    print(startup())
    extractedRows = userInput([], [0, 0])
    binpackInput = initiateParams(extractedRows)
    displaySelectedRows(binpackInput)


main()
