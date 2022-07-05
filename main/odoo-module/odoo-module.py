"""
Author: Elvis Obero-Atkins
Last Edited by: Elvis Obero-Atkins

This py script is NOT REQUIRED for yandiya-cbm-library to function

It is odoo module written in python designed to interact with the yandiya-cbm-library.
"""
####################################################################################
#"import cbmcalculator as cbm" should not be up here! if it is move to other comment
####################################################################################
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
####################################################################################
#the line "import cbmcalculator as cbm" ALWAYS needs to be below the above lines ###
import cbmcalculator as cbm
####################################################################################