"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This is the __init__.py script, it is what enables the ability to make the cbm library - 
which previously was all contained in the file cbmcalculator.py into a local package

It also allows me to decompose the fucntions of the calculator 
into modules which is better programming practice

Call the following functions in order to use the calculator effectively (in it's current local form):
- search_product() and input a string
- parameters() and input the output from search_product() and a integer
- ...
"""

# how to use: call search_product to access database, use parameters to create input-list then...

from yandiyacbm.search_product import search_product
from yandiyacbm.headings import productdetails_headings, palletdetails_headings
from yandiyacbm.parameters import parameters
from yandiyacbm.bin_packing import shipping, bin_select, bin_iniate, packing

# TODO:
# - Shipping_Logic is just a basic implementation of the fucntion, Implement excel functionality
# - refactor code in cli-app loop
# - look at php 4d bin packing libarary and how it lays out functions
# - creation of bins etc