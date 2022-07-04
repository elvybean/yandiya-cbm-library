"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""


def multiplierCreate(inValue: float, L_value: float, S_value: float):
    # recursive code from shipping_logic
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
    # FIXME: Get accurate values for Parcel Force: Dimensions so you know the maximum cbm
    """calculates using simple logic whether or not a item needs to be send via parcel or package
    Args:
        weight (float): _description_

    Returns:
        string: value of parcel or pallet, depending on outcome of logic
    """

    """
    if weight <= 30:
        if cbm <= 3:  # this is a placeholder value as I currently don't know maxmimum CBM for parcels
            return ["parcel-force", 1]
        else:
            multiplier = round(cbm/3)
            return ["parcel-force", multiplier]
        
    """

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

    else:
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
