# TODO:
# - Shipping_Logic is just a basic implementation of the fucntion, Implement excel functionality
# - refactor code in cli-app loop
# - look at php 4d bin packing libarary and how it lays out functions
# - creation of bins etc

#how to use: call search_product to access database, use parameters to create input-list then...

from yandiyacbm.search_product import search_product
from yandiyacbm.headings import productdetails_headings, palletdetails_headings
from yandiyacbm.parameters import parameters
from yandiyacbm.bin_packing import shipping
