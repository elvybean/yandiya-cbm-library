"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
    
def productdetails_headings():
    """returns the headings of the product-details sheet
    Args:
        (none)
    Returns:
        list: stores all the headings for each of the columns
    """
    return ['partNo', 'barcode', 'sku', 'productTitle', 'icWidth', 'icHeight', 'icDepth', 'icWeight', 'icQty', 'ocWidth', 'ocHeight', 'ocDepth', 'ocWeight', 'ocQty']  # 14 (0-13) Items in list



def palletdetails_headings():
    """returns the headings of the pallet-shipping sheet
    Args:
        (none)
    Returns:
        list: stores all the headings for each of the columns
    """
    return ['name', 'length', 'width', 'height', 'cbm', 'maxWeight', 'price']  # 7 (0-6) Items in list
