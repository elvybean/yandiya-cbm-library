"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This is the __init__.py script, it is what enables the ability to make the cbm library - 
which previously was all contained in the file cbmcalculator.py into a local package

It also allows me to decompose the fucntions of the calculator 
into modules which is better programming practice
"""

from yandiyacbm.excel_func import search_products, parameters_generate, divider, parameters_display
#from yandiyacbm.excel_utils import divider
#from yandiyacbm.py4dbp import Item, Bin, Packer
from yandiyacbm.py4dbp_utils import binpack_start_prints#, initiate_pallets, pallet_select_prints, pre_pack, re_pack


# TODO:
#- make output format of products in yandiyacbm equal to the input format of py4dbp
#- further remove and refactor py4dbp so it contains only what is required.
#- make py4dbp stop packing once it's found a compatible bin.
#- further refactor yandiyacbm to make it more professional, object oriented?
