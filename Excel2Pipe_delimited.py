#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Objective: Convert excel file to pipe delimited file or any other delimeter
Author: Rinkesh Jindal
Date:   17-Arp-2020

Usage: Excel2Pipe_delimited2.py file.xlsx file.csv
"""

import pandas as pd
import os.path as path
import sys

#check if incorrect arguments passed 
if len(sys.argv)<3:
    print("Please use this as> Excel2Pipe_delimited2.py file.xlsx file.csv")
    sys.exit()

#print(sys.argv) #check Arguments passed for debugging
in_file = sys.argv[1]
out_file = sys.argv[2]
delimiter = "|"

if path.isfile(in_file): #check is file exists
    print("Reading "+in_file+" file")
    read_file = pd.read_excel(in_file) #read file
    print("Completed reading "+in_file+" file")
else:
    print("Check path/file name as unable to find: "+in_file)
    sys.exit()

read_file.to_csv(out_file, index = None, header=True, sep=delimiter) #convert the file
print("Created "+out_file+" file")