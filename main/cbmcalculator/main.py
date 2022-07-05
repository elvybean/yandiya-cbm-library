"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
from . import calculate as cal
from . import shipping_logic as shl

# TODO:
# - Shipping_Logic is just a basic implementation of the fucntion, Implement excel functionality
# - Refactor calculate function to output additional information, product dimensions
# - Implement Knapsack / Bin Packing Problem algorithms for pallet selection to allow it to consider;
#       dimensions as well as weight and cbm & so it doesn't assume the products are malluable.
# - Implement use of PostgresSQL instead of excel


def main(parameters: list):
    """main function of the py script
    Args:
        parameters (list): is a list of lists that containa stored extracted excel rows as a list and user inputted integer quanities
        (3 Dimensional List)

    Returns:
        list: stores the calculated total cbm, the total weight and how the item will be shipped.
    """
    # parameters = [ [ [Excel Row List], Item Quantity Integer ] , ... ]
    totalCBM = 0
    totalWeight = 0
    bin_pack_parameters = []

    for i in range(len(parameters)):
        j = parameters[i]
        k = cal.calculate(j[0], j[1])
        totalCBM += k[0]
        totalWeight += k[1]
        bin_pack_parameters.append([k[2],k[3]])

    stack_layout = shl.shipping_logic(totalCBM, totalWeight, bin_pack_parameters)

    return [totalCBM, totalWeight, bin_pack_parameters, stack_layout]
