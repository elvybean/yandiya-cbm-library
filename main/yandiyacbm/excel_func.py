"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
import openpyxl
from openpyxl import Workbook


def search_products(SearchParams: str):
    """searches a database document based on user input of a product number, barcode or sku
    Args:
        parameters (string): a product number, barcode or sku that the
                            user inputted for the purpose of using to search the database
    Returns (conditional):
        list: stores the extracted database row (if row can be found in database)
        int: 0 (if row cannot be found in database)
    """
    yandiya_db = openpyxl.load_workbook(
        'database\yandiya-db.xlsx')
    records_table = yandiya_db.active

    if len(SearchParams) == 5:
        search_column = records_table['C']  # sku
    elif len(SearchParams) == 13:
        search_column = records_table['B']  # barcode
    else:
        search_column = records_table['A']  # partNo

    requiredData = 0
    for cell in search_column:
        if cell.value == SearchParams:
            requiredData = records_table[cell.row]
            break

    if requiredData == 0:
        return 0

    extractedRows = []
    for cell in requiredData:
        extractedRows.append(cell.value)

    return extractedRows


def multiple_row_format(extractedRows: list):
    formattedData = []
    for i in range(len(extractedRows)):
        product = extractedRows[i]
        formatted = row_format(product[0], product[1])
        formattedData.append(formatted)
    return formattedData


def row_format(row: list, itemQuantity: int):
    if itemQuantity >= (int(row[13]) / 2):
        if itemQuantity > int(row[13]):

            remainderItems = itemQuantity % float(row[13])
            divisable = itemQuantity - remainderItems
            outerCartons = divisable / float(row[13])

            if remainderItems >= (float(row[13]) / 2):
                outerCartons += 1
                innerCartons = 0
            else:
                innerCartons = remainderItems
        else:
            outerCartons = 1
            innerCartons = 0
    else:
        outerCartons = 0
        innerCartons = itemQuantity

    funcOutput = [[row[3], row[0], itemQuantity]]

    if innerCartons != 0:
        icList = [row[3] + " Inner Carton", row[4], row[5], row[6], row[7]]
        for i in range(int(innerCartons)):
            funcOutput.append(icList)

    if outerCartons != 0:
        ocList = [row[3] + " Outer Carton", row[9], row[10], row[11], row[12]]
        for i in range(int(outerCartons)):
            funcOutput.append(ocList)

    return funcOutput
