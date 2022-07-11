"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
from yandiyacbm.misc import extract

def shipping_approx(values: list):  # legacy function
    """using the cbm and weight values of an item, calculates which pallet type would be most appropriate
    Args:
        params (list): contains the items name and dimensions, weight and cbm for inner and outer cartons (if applicable)
    Returns:
        list: contains a string value that repersents the pallet that needs to be used 
            to send the items and a integer value that repersents how many are needed
    """
    cbm = values[0]
    weight = values[1]

    if cbm <= 0.768 and weight <= 300:
        return ["euro-quarter", 1]

    elif cbm <= 1.152 and weight <= 300:
        return ["standard-quarter", 1]

    elif cbm <= 1.152 and weight <= 600:
        return ["euro-half", 1]

    elif cbm <= 1.728 and weight <= 600:
        return ["standard-half", 1]

    if cbm <= 2.112 and weight < 1200:
        return ["euro-full", 1]

    elif cbm <= 3.168 and weight < 1200:
        return ["standard-full", 1]

    else:
        weight_multiplier = round(weight / 1200)
        return ["standard-full", weight_multiplier]
