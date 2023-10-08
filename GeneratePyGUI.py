"""
Created on 07.10.2023
@author: mat-eng
@description: convert .ui file to .py
"""
########################################################################################################################
# Import libraries
import os

########################################################################################################################
# Convert Qt .ui interface in .py
print("Start converting .ui interface into .py")
os.system("pyuic5 main_window.ui -o main_window.py")
print(".ui to .py conversion done.")
