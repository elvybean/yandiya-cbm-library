"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""

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

def shipping(params: list): 
    cbm = 0
    weight = 0

    if params[1] != "NULL":
        cbm += params[1][1]
        weight += params[1][2]

    if params[2] != "NULL":
        cbm += params[2][1]
        weight += params[2][2]
        
        

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
