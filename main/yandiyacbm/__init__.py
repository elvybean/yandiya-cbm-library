"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This is the __init__.py script, it is what enables the ability to make the cbm library - 
which previously was all contained in the file cbmcalculator.py into a local package

It also allows me to decompose the fucntions of the calculator 
into modules which is better programming practice
"""

from yandiyacbm.excel_func import search_products, parameters_generate, parameter_list
from yandiyacbm.excel_utils import productdetails_headings, palletdetails_headings
from yandiyacbm.py4dbp import Order, Item, Bin, Packer
from yandiyacbm.py4dbp_utils import binpack, initiate_pallets, pallet_select, pre_pack, re_pack
from yandiyacbm.output import parameters_display, binpack_prints, pallet_select_prints, order_output


# TODO:
# - further refactor yandiyacbm to make it more professional, object oriented?
# - remove other bins once correct bin is found
