"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
import openpyxl
from openpyxl import Workbook


def search_product(parameters: str):
    """searches a database document based on user input of a product number, barcode or sku
    Args:
        parameters (string): a product number, barcode or sku that the
                            user inputted for the purpose of using to search the database
    Returns (conditional):
        list: stores the extracted database row (if row can be found in database)
        int: 0 (if row cannot be found in database)
    """
    yandiya_db = openpyxl.load_workbook(
        'main\database\yandiya-db.xlsx')
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


def parameter_generate(row: list, itemQuantity: int):  # legacy
    # Three possible outcomes; "x of Oyter Cartons", "x of Inner Cartons" and "x of Oyter Cartons AND x of Inner Cartons"
    if itemQuantity >= (int(row[13]) / 2):
        if itemQuantity > int(row[13]):  # x of Outer Cartons

            remainderItems = itemQuantity % float(row[13])
            divisable = itemQuantity - remainderItems
            outerCartons = divisable / float(row[13])

            if remainderItems >= (float(row[13]) / 2):
                outerCartons += 1
                innerCartons = 0
            else:  # x of Oyter Cartons AND x of Inner Cartons
                innerCartons = remainderItems
        else:
            outerCartons = 1
            innerCartons = 0
    else:  # x of Inner Cartons
        outerCartons = 0
        innerCartons = itemQuantity

    output = [[row[3], row[0], itemQuantity]]

    # this is the accepted format by packer()
    # 'IH35-W Outer Carton', 700.0, 710.0, 250.0, 25.9
    # 'IH35-W Outer Carton', 700.0, 710.0, 250.0, 25.9
    # 'IH35-W Inner Carton', 670.0, 660.0, 50.0, 4.78
    # 'IH35-W Inner Carton', 670.0, 660.0, 50.0, 4.78

    # curretnly is in:
    # ['IH35-W', [2.0, 0.04422, 9.56, 670.0, 660.0, 50.0, 4.78], [2.0, 0.2485, 51.84, 700.0, 710.0, 250.0, 25.92]]

    # easiest solution would to be to get it into
    # [['IH35-W Outer Carton', 700.0, 710.0, 250.0, 25.9], ['IH35-W Outer Carton', 700.0, 710.0, 250.0, 25.9]
    #                                                      , ['IH35-W Inner Carton', 670.0, 660.0, 50.0, 4.78], ['IH35-W Inner Carton', 670.0, 660.0, 50.0, 4.78]]

    # This will later have to be seperated into another

    if innerCartons != 0:
        icList = [row[3] + " Inner Carton", row[4], row[5], row[6], row[7]]
        for i in range(int(innerCartons)):
            output.append(icList)

    if outerCartons != 0:
        ocList = [row[3] + " Outer Carton", row[9], row[10], row[11], row[12]]
        for i in range(int(outerCartons)):
            output.append(ocList)

    return output
