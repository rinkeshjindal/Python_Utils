
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
import duplicateFileFinder as dFF

if len(sys.argv) == 1:
    # Print usage
    print("Usage: del_EmptyFilesFolders.py ""C:/Test""")
    exit
else:
    source_path = sys.argv[1]
try:
    all_files = pd.read_csv(source_path + "/All_files_2.csv",index_col=0)
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

#values of duplicate_files columns 'checksum' and 'filename' that will be used to filter df1
    idxs = list(zip(duplicate_files.checksum.values, duplicate_files.filename.values, duplicate_files.path.values))

    #so all_files is filtered based on the values present in columns of df2 (idxs)
    all_files = all_files[~pd.Series(list(zip(all_files.checksum, all_files.filename, all_files.path)), index=all_files.index).isin(idxs)]
    
    #Matching on index in two df
    #all_files.drop(duplicate_files.index, inplace = True)

    # Delete existing files
    filelist = pd.DataFrame(
        columns=["checksum", "filename", "path", "size", "owner", "accesstime", "modifytime", "createtime"])

    # details structure is checksum, filename, path, size, owner, accesstime, modifytime, createtime
    file_types_inscope = ["ppt", "pptx", "pdf", "txt", "mp4", "html", "DAT", "jpg", "jpeg", "bmp", "doc", "docx", "xls",
                          "xlsx"]

    # Walk through all files and folders within directory
    for path, dirs, files in os.walk(source_path):
        # print("Analyzing {}".format(path))
        for each_file in files:
            #print(each_file)
            if each_file.split(".")[-1].lower() in file_types_inscope:
                tmplist = []

                # The path variable gets updated for each subfolder
                file_path = os.path.join(os.path.abspath(path), each_file)

                md5_code = dFF.generate_md5(file_path)
                #try:
                #print(file_path)
                #print(all_files[['checksum']].isin([md5_code]).any().any())
                if all_files[['checksum']].isin([md5_code]).any().any():
                    print(print(all_files[['checksum']].isin([md5_code]).any().any()))
                    #if os.path.isFile(file_path):
                    os.remove(file_path)
                    print("Removed")
                #except:
                else:
                    print(file_path + " Error with file attributes")
                    #print(err + " Error with file attributes")

except:
    print("either all files or duplicates not exists")
    pass

print(all_files.shape)
all_files.to_csv(source_path +"/All_files.csv")
