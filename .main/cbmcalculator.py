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
        # checks if item quanity is >= half of the maximum amount
        # of items that can go inside a outer carton

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

    for i in range(len(parameters)):
        tempStore = parameters[i]
        calculations = calculate(tempStore[0], tempStore[1])
        cbm += calculations[0]
        weight += calculations[1]

    shipping = shipping_logic(cbm, weight)

    return [cbm, weight, shipping]


def shipping_logic(cbm: float, weight: float):
    # renamed weight_logic to shipping_logic
    """calculates using simple logic whether or not a item needs to be send via parcel or package
    Args:
        weight (float): _description_

    Returns:
        string: value of parcel or pallet, depending on outcome of logic
    """
    # compares cbm & weight of products to cbm & weight of pallet and finds the most appropriate

    # MVP: this is a basic implementation of the fucntion, just using strings and set values
    # instead of some form of database (.xlsx or SQL)
    match weight:
        case _ if weight <= 30:
            type = "parcel-force"

        case _ if not weight <= 30 and weight <= 300:
            if cbm <= 0.768:
                return ["euro-quarter", round(float(cbm/0.768))]
            else:  # (cbm > 0.768 and cbm <= 1.152):
                return ["standard-quarter", round(float(cbm/1.152))]

        case _ if not weight <= 300 and weight <= 600:
            if (cbm <= 1.152):
                return ["euro-half", round(float(cbm/1.152))]
            else:  # (cbm > 1.152 and cbm <= 1.728):
                type = "standard-half"
                return ["standard-half", round(float(cbm/1.728))]

        case _ if not weight <= 600 and weight <= 1200:
            if (cbm <= 2.112):
                return ["euro-full", round(float(cbm/2.112))]
            else:  # (cbm > 2.112 and cbm <= 3.168):
                return ["standard-full", round(float(cbm/3.168))]


def productdetails_headings():
    """returns the headings of the product-details sheet
    Returns:
        list: stores all the headings for each of the columns
    """
    return ['partNo', 'barcode', 'sku', 'productTitle', 'pWidth', 'pHeight', 'pDepth', 'icWidth', 'icHeight',
            'icDepth', 'icWeight', 'icQty', 'ocWidth', 'ocHeight', 'ocDepth', 'ocWeight', 'ocQty']  # 17 (0-16) Items in list


def shippingdetails_headings():
    """returns the headings of the pallet-shipping sheet
    Returns:
        list: stores all the headings for each of the columns
    """
    return ['name', 'length', 'width', 'height', 'cbm', 'maxWeight', 'price']  # 7 (0-6) Items in list
