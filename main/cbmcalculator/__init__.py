# TODO:
# - Shipping_Logic is just a basic implementation of the fucntion, Implement excel functionality
# - Refactor calculate function to output additional information, product dimensions
# - Implement Knapsack / Bin Packing Problem algorithms for pallet selection to allow it to consider;
#       dimensions as well as weight and cbm & so it doesn't assume the products are malluable.
# - Implement use of PostgresSQL instead of excel

#from cbmcalculator.main import main
from cbmcalculator.calculate import calculate
from cbmcalculator.bin_packing import bin_packing
from cbmcalculator.search_product import search_product
from cbmcalculator.headings import productdetails_headings, palletdetails_headings