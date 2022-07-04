"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""


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

        if itemQuantity > int(parameters[16]):
            remainderItems = itemQuantity % int(parameters[16])
            ocDividable = itemQuantity - remainderItems
            ocMultiply = ocDividable / int(parameters[16])

            if remainderItems >= (int(parameters[16]) / 2):
                ocMultiply += 1

            else:
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
