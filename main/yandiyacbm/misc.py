"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
def calculate(width: float, height: float, depth: float, weight: float, quantity: int):
    """calculates the total CBM and total weight of an item based on inputted values
    Args:
        width (float): width of item in mm
        height (float): height of item in mm
        depth (float): depth of item in mm
        weight (float): weight of item
        quantity (int): quantity of item
    Returns:
        list [float/int, float/int]: this is a list that contains the calculated total cbm and 
                                    total weight of the item whose values were inputted
    """
    return [((width * height * depth / 1000000000) * quantity), (weight * quantity)]

def extract(parameters: list):
    """extarcts the total cbm and total weight of a product, adding its IC and OC values together
    Args:
        parameters (list): list containing a product's name, cbm, weight and ic and oc details
    Returns:
        list: extracted total cbm and total weight in a list
    """
    cbm = 0
    weight = 0


    if parameters[1] != "NULL":
        cbm += parameters[1][1]
        weight += parameters[1][2]

    if parameters[2] != "NULL":
        cbm += parameters[2][1]
        weight += parameters[2][2]

    return [cbm, weight]
