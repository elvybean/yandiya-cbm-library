"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""


def icCBM():
    return 0


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
            ocDividable = itemQuantity - remainderItems
            ocMultiply = ocDividable / float(parameters[13])

            # x of Oyter Cartons
            if remainderItems >= (float(parameters[13]) / 2):
                ocMultiply += 1
                icMultiply = 0

                dimensions = ["OC", float(parameters[9]), float(
                    parameters[10]), float(parameters[11]), ocMultiply]

            else:  # x of Oyter Cartons AND x of Inner Cartons
                icMultiply = remainderItems

                dimensions = ["Both", float(parameters[4]), float(parameters[5]), float(parameters[6]), icMultiply, float(
                    parameters[9]), float(parameters[10]), float(parameters[11]), ocMultiply]

                # cbm += ((float(parameters[4]) * float(parameters[5]) *
                #        float(parameters[6]) / 1000000) * remainderItems)
                #weight += (float(parameters[7]) * remainderItems)

        else:
            ocMultiply = 1
            icMultiply = 0

        cbm += (float(parameters[9]) * float(parameters[10])
                * float(parameters[11]) / 1000000) * ocMultiply
        weight += float(parameters[12]) * ocMultiply

    else:  # x of Inner Cartons
        icMultiply = itemQuantity

        dimensions = ["IC", float(parameters[4]), float(
            parameters[5]), float(parameters[6]), itemQuantity]

        # cbm = ((float(parameters[4]) * float(parameters[5]) *
        #        float(parameters[6]) / 1000000) * itemQuantity)
        #weight = (float(parameters[7]) * itemQuantity)

    cbm += ((float(parameters[4]) * float(parameters[5]) *
             float(parameters[6]) / 1000000) * icMultiply)
    weight += (float(parameters[7]) * icMultiply)

    #dimensions = []

    return [cbm, weight]
    # return [cbm, weight, dimensions] #returns CBM, weight and dimesnions in a list (W x H x D)
