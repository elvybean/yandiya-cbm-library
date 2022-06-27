"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is main component of the yandiya-cbm-library
As well as this py script the yandiya-db.xslx (excel file) is required

"""
import openpyxl
from openpyxl import Workbook


def searching_product(parameters):
    """searches an excel document based on user input of a product number, barcode or sku
    Args:
        parameters (string): a product number, barcode or sku that the 
                            user is using to search the excel for

    Returns:
        list: stores the extracted excell row (if found)
        int: 0 (if row not found)
    """
    yandiya_db = openpyxl.load_workbook(
        '.main\yandiya-db.xlsx')
    records_table = yandiya_db.active

    if len(parameters) == 5:
        search_column = records_table['C']  # sku
    elif len(parameters) == 13:
        search_column = records_table['B']  # barcode
    else:
        search_column = records_table['A']  # partNo

    requiredData = 0
    for cell in search_column:
        if cell.value == parameters:
            requiredData = records_table[cell.row]
            break

    if requiredData == 0:
        return 0

    returnValue = []
    for cell in requiredData:
        returnValue.append(cell.value)

    return returnValue


def calculate(parameters: list, itemQuantity: int):
    """searches a list variable for specific values and then calculates and returns cbm and total weight
    Args:
        parameters (list): stored extracted excel row
        itemQuantity (int): user inputted item quanitiy to be 
            used in calculations

    Returns:
        list: stores the calculated cbm and the total weight
    """
    if itemQuantity >= (float(parameters[16]) / 2):

        cbm = (int(parameters[12]) * int(parameters[13])
               * int(parameters[14]) / 1000000)

        weight = float(parameters[15])

    else:

        cbm = ((int(parameters[7]) * int(parameters[8]) *
                int(parameters[9]) / 1000000) * itemQuantity)

        weight = (float(parameters[10]) * itemQuantity)

    return [cbm, weight]


def calculate_multiple(parameters: list):
    """n/a
    Args:
        parameters (list): is a list of lists that containa stored extracted excel rows as a list and user inputted integer quanities 
        (3 Dimensional List)

    Returns:
        list: stores the calculated total cbm, the total weight and how the item will be shipped.
    """
    # Main List = [ [Secondary List = [Third List(Excel Row), Integer] ] , [ y ], [ z ] ]
    cbm = 0
    weight = 0

    # iterate over number of lists in list of lists
    # feed the smaller lists into calculate() as it's parameters
    # adds returned values to cbm and weight respectively
    # return total values of cbm and weight

    for i in range(len(parameters)):
        tempStore = parameters[i]
        calculations = calculate(tempStore[0], tempStore[1])
        cbm += calculations[0]
        weight += calculations[1]

    shipping = weight_logic(weight)

    return [cbm, weight, shipping]


def weight_logic(weight: float):
    """calculates using simple logic whether or not a item needs to be send via parcel or package
    Args:
        weight (float): _description_

    Returns:
        string: value of parcel or pallet, depending on outcome of logic
    """
    if weight <= 30:
        return "Parcel"
    else:
        return "Pallet"


def productdetails_headings():
    """returns the headings of the product-details sheet
    Returns:
        list: stores all the headings for each of the columns
    """
    return ['partNo', 'barcode', 'sku', 'productTitle', 'pWidth', 'pHeight', 'pDepth', 'icWidth', 'icHeight',
            'icDepth', 'icWeight', 'icQty', 'ocWidth', 'ocHeight', 'ocDepth', 'ocWeight', 'ocQty']  # 17 (0-16) Items in list
