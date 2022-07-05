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

    # Three possible outcomes; "x of Oyter Cartons", "x of Inner Cartons" and "x of Oyter Cartons AND x of Inner Cartons"

    if itemQuantity >= (int(parameters[13]) / 2):

        if itemQuantity > int(parameters[13]):

            remainderItems = itemQuantity % float(parameters[13])
            x = itemQuantity - remainderItems
            ocMultiply = x / float(parameters[13])

            # x of Oyter Cartons
            if remainderItems >= (float(parameters[13]) / 2):
                ocMultiply += 1
                icMultiply = 0

                bin_pack = ["OC", float(parameters[9]), float(
                    parameters[10]), float(parameters[11]), ocMultiply]

            else:  # x of Oyter Cartons AND x of Inner Cartons
                icMultiply = remainderItems

                bin_pack = ["Both", float(parameters[4]), float(parameters[5]), float(parameters[6]), icMultiply, float(
                    parameters[9]), float(parameters[10]), float(parameters[11]), ocMultiply]

        else:
            ocMultiply = 1
            icMultiply = 0

        cbm += (float(parameters[9]) * float(parameters[10])
                * float(parameters[11]) / 1000000) * ocMultiply
        weight += float(parameters[12]) * ocMultiply

    else:  # x of Inner Cartons
        icMultiply = itemQuantity

        bin_pack = ["IC", float(parameters[4]), float(
            parameters[5]), float(parameters[6]), itemQuantity]

    cbm += ((float(parameters[4]) * float(parameters[5]) *
             float(parameters[6]) / 1000000) * icMultiply)
    weight += (float(parameters[7]) * icMultiply)

    # returns CBM, weight and dimesnions in a list (W x H x D)
    return [cbm, weight, parameters[0], bin_pack]
