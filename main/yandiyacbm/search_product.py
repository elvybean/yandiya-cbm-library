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
