"""
Author: Elvis Obero-Atkins Last 
Edited by: Elvis Obero-Atkins 

This file is NOT REQUIRED for yandiya-cbm-library to function 
It is a py script written written for the HTML page of the same name designed to interact with the yandiya-cbm-library. 
"""
from datetime import date 
today = date.today()
print("Today's date:", today)

#######################################################################################
#import yandiyacbm as yandiya should not be up here! if it is move to other comment ###
#######################################################################################
import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    os.pardir)
)
sys.path.append(PROJECT_ROOT)
#######################################################################################
#import yandiyacbm as yandiya ALWAYS needs to be below import os and import sys #######
#######################################################################################
import yandiyacbm as yandiya ##########################################################
#######################################################################################

modulename = "yandiya"
if modulename not in sys.modules:
    print ("You have not imported the yandiya module")
elif modulename in sys.modules:
    print ("You have imported the yandiya module")
else:
    print("error?")