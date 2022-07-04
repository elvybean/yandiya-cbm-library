"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""
import calculate as cal
import shipping_logic as shl


def main(parameters: list):
    """main function of the py script
    Args:
        parameters (list): is a list of lists that containa stored extracted excel rows as a list and user inputted integer quanities
        (3 Dimensional List)

    Returns:
        list: stores the calculated total cbm, the total weight and how the item will be shipped.
    """
    # Main List = [ [ [Excel Row], Integer ] , [ [Excel Row], Integer ], [ [Excel Row], Integer ] ]
    cbm = 0
    weight = 0

    for i in range(len(parameters)):
        tempStore = parameters[i]
        calculations = cal(tempStore[0], tempStore[1])
        cbm += calculations[0]
        weight += calculations[1]

    shipping = shl(cbm, weight)

    return [cbm, weight, shipping]
