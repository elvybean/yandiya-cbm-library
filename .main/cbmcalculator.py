"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is main component of the yandiya-cbm-library
As well as this py script the yandiya-db.xslx (excel file) is required

modify calculate function for additional information, such as IC and OC quanity + dimensions
refactor calculate fucntion. (3D Calculations)

"""
import openpyxl
from openpyxl import Workbook


def search_product(parameters):
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
    cbm = 0
    weight = 0

    if itemQuantity >= (int(parameters[16]) / 2):
        # checks if item quanity is >= half of the maximum amount of items that can go inside a outer carton

        # creates a multiplier for amount of outer cartons
        if itemQuantity > int(parameters[16]):
            remainderItems = itemQuantity % int(parameters[16])
            ocDividable = itemQuantity - remainderItems
            ocMultiply = ocDividable / int(parameters[16])

            if remainderItems >= (int(parameters[16]) / 2):
                ocMultiply += 1

            else:
                # the remainder of items are packaged in inner cartons
                cbm += ((int(parameters[7]) * int(parameters[8]) *
                        int(parameters[9]) / 1000000) * remainderItems)

                weight += (float(parameters[10]) * remainderItems)

        else:
            ocMultiply = 1

        cbm += (int(parameters[12]) * int(parameters[13])
                * int(parameters[14]) / 1000000) * ocMultiply

        weight += float(parameters[15]) * ocMultiply

    else:

        cbm = ((int(parameters[7]) * int(parameters[8]) *
                int(parameters[9]) / 1000000) * itemQuantity)

        weight = (float(parameters[10]) * itemQuantity)

    return [cbm, weight]


def multiplierCreate(inValue: float, L_value: float, S_value: float):
    # used in shipping logic fucntion multiple time,
    # made sense to make into a seperate function to reuse
    L_remainder = inValue % L_value
    L_dividable = inValue - L_remainder
    L_multiplier = L_dividable / L_value

    if L_remainder > S_value:
        S_remainder = L_remainder % S_value
        S_dividable = L_remainder - S_remainder
        S_multiplier = S_dividable / S_value
        S_multiplier += 1
    else:
        S_multiplier = 1

    return [round(L_multiplier), round(S_multiplier)]


def shipping_logic(cbm: float, weight: float):
    # renamed weight_logic to shipping_logic
    """calculates using simple logic whether or not a item needs to be send via parcel or package
    Args:
        weight (float): _description_

    Returns:
        string: value of parcel or pallet, depending on outcome of logic
    """
    # MVP: this is a basic implementation of the fucntion, just using strings and set values
    # instead of some form of database (.xlsx or SQL)

    if weight <= 300:
        if cbm <= 0.768:
            return ["euro-quarter", 1]
        elif cbm <= 1.152:
            return ["standard-quarter", 1]
        else:
            multipliers = multiplierCreate(cbm, 1.152, 0.768)
            return ["standard-quarter", multipliers[0], "euro-quarter", multipliers[1]]

    elif weight <= 600:
        if cbm <= 1.152:
            return ["euro-half", 1]
        elif cbm <= 1.728:
            return ["standard-half", 1]
        else:
            multipliers = multiplierCreate(cbm, 1.728, 1.152)
            return ["standard-half", multipliers[0], "euro-half", multipliers[1]]

    else:  # weight > 600 and weight < 1200:
        if cbm <= 2.112 and weight < 1200:
            return ["euro-full", 1]
        elif cbm <= 3.168 and weight < 1200:
            return ["standard-full", 1]
        else:
            weight_multiplier = round(weight / 1200)
            multipliers = multiplierCreate(cbm, 3.168, 2.112)
            if (multipliers[0] + multipliers[1]) < weight_multiplier:
                multipliers[1] += 1
            return ["standard-full", multipliers[0], "euro-full", multipliers[1]]


def main(parameters: list):
    """n/a
    Args:
        parameters (list): is a list of lists that containa stored extracted excel rows as a list and user inputted integer quanities
        (3 Dimensional List)

    Returns:
        list: stores the calculated total cbm, the total weight and how the item will be shipped.
    """
    # Main List = [ [ [Excel Row], Integer ] , [ [Excel Row], Integer ], [ [Excel Row], Integer ] ]
    cbm = 0
    weight = 0

    for i in range(len(parameters)):
        tempStore = parameters[i]
        calculations = calculate(tempStore[0], tempStore[1])
        cbm += calculations[0]
        weight += calculations[1]

    shipping = shipping_logic(cbm, weight)

    return [cbm, weight, shipping]


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
