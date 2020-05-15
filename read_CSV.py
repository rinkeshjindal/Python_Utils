#-------------------------------------------------------------
#    read_CSV.py
#    Deletes all empty folders under a given path.
#    
#    Created on May 15, 2020
#
# author: Rinkesh_Jindal
#
#    Usage: del_EmptyFilesFolders.py "C:/Test"
#-------------------------------------------------------------

import sys, os
import pandas as pd

if len(sys.argv) == 1:
    # Print usage
    print("Usage: del_EmptyFilesFolders.py ""C:/Test""")
    exit
else:
    source_path = sys.argv[1]
try:
    all_files = pd.read_csv(source_path + "/all_files_2.csv",index_col=0)
    print(all_files.shape)
    print(all_files[['checksum','filename','path']].head(5))
    duplicate_files = pd.read_csv(source_path + "/duplicates_2.csv",index_col=0)
    print(duplicate_files.shape)
    print(duplicate_files[['checksum','filename','path']].head(5))

    print("TTT")

#     cond = all_files[['checksum','filename','path']].isin(duplicate_files[['checksum','filename','path']])
#     print(cond.head(5))
#     print(cond.shape)
#    all_files.drop(all_files[cond].index, inplace = True)
    all_files.drop(duplicate_files.index, inplace = True)
except:
    print("either all files or duplicates not exists")
    pass

print(all_files.shape)
all_files.to_csv(source_path +"/All_files.csv")
