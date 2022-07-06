"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""

# takes params

def packing(): #takes bins and items as parameters
    # packing products into bins 
    return 0

def bin_iniate():
    #call this before any other fucntions to create 
    #   global bin variable lists
    # OR use bin select to iniate bins instead
    #   research and consider what would be easier
    return 0

def bin_select(products: list):
    #check total weight/cbm of all products
    #  and use these values to find the most appropriate pallet
    #i.e instead of two 300kg pallets costs £33 each (£66) use 1 600kg pallet which costs £35
    return 0


#no longer used below, its legacy code
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
"""


def shipping(params: list): #legacy
    # FIXME: Get accurate values for Parcel Force: Dimensions so you know the maximum cbm

    cbm = 0
    weight = 0

    if params[1] != "NULL":
        cbm += params[1][1]
        weight += params[1][2]

    if params[2] != "NULL":
        cbm += params[2][1]
        weight += params[2][2]

    """
    if weight <= 30:
        if cbm <= 3:  # this is a placeholder value as I currently don't know maxmimum CBM for parcels
            return ["parcel-force", 1]
        else:
            multiplier = round(cbm/3)
            return ["parcel-force", multiplier]
        
    """


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
