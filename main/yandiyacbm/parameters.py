"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
from yandiyacbm.misc import calculate

def parameters(row: list, itemQuantity: int): #legacy
    parameters = [row[0]]
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


    # this needs changing
    if innerCartons != 0:
        inner = calculate(float(row[4]), float(row[5]), float(
            row[6]), float(row[7]), innerCartons)
        parameters.append([innerCartons, inner[0], inner[1], float(
            row[4]), float(row[5]), float(row[6]), float(row[7])])
    else:
        parameters.append("NULL")

    if outerCartons != 0:
        outer = calculate(float(row[9]), float(row[10]), float(
            row[11]), float(row[12]), outerCartons)
        parameters.append([outerCartons, outer[0], outer[1], float(
            row[9]), float(row[10]), float(row[11]), float(row[12])])
    else:
        parameters.append("NULL")

    return parameters

