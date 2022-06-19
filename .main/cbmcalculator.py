"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is main component of the yandiya-cbm-library
As well as this py script the yandiya-db.xslx (excel file) is required

This is V0.1.1 of the yandiya-cbm-library
It meets three milestones outlined in the proposal

To Do:
- logic for height considerations for pallet
- maximum length for parcels which is 3 meters
- Postcode logic - 2832 to consider
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

    reqData = 0
    for cell in search_column:
        if cell.value == parameters:
            reqData = records_table[cell.row]
            break

    if reqData == 0:
        return 0

    output = []
    for cell in reqData:
        output.append(cell.value)

    return output


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

        # if float(parameters[15]) <= 30:
        #    sendWith = "Parcel"
        # else:
        #    sendWith = "Pallet"

        cbm = (int(parameters[12]) * int(parameters[13])
               * int(parameters[14]) / 1000000)

        weight = float(parameters[15])

    else:

        # if (float(parameters[10]) * itemQuantity) <= 30:
        #    """ ValueError: invalid literal for int() with base 10: '4.78' on Line 52 """
        #    sendWith = "Parcel"
        # else:
        #    sendWith = "Pallet"

        cbm = ((int(parameters[7]) * int(parameters[8]) *
                int(parameters[9]) / 1000000) * itemQuantity)

        weight = (float(parameters[10]) * itemQuantity)

    return [cbm, weight]


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
            'icDepth', 'icWeight', 'icQty', 'ocWidth', 'ocHeight', 'ocDepth', 'ocWeight', 'ocQty']  # 17 (0 -16) Items in list
