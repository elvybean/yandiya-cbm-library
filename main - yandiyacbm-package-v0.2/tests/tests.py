"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins
"""

def startup(): # this is unnecessary but cool
    f = open("main/tests/tests.txt", "r")
    value = (f.read())
    f.close()
    return value