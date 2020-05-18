
"""
Input Source folder, traverse through all files within the folder and subfolders
and get list of all files that are duplicates using md5 checcksum for each file 
"""

import os
import hashlib
from collections import defaultdict
import csv
import stat
import time
import pandas as pd
import shutil
#from builtins import False

#src_folder = "C:/Users/rinkesh_jindal/Downloads"
src_folder = "D:/Online Data/temp"

def generate_md5(fname, chunk_size=1024):
    """
    Function which takes a file name and returns md5 checksum of the file
    """
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        # Read the 1st block of the file
        chunk = f.read(chunk_size)
        # Keep reading the file until the end and update hash
        while chunk:
            hash.update(chunk)
            chunk = f.read(chunk_size)

    # Return the hex checksum
    return hash.hexdigest()


if __name__ == "__main__":
    """
    Starting block of script
    """

    # The dict will have a list as values
    md5_dict = defaultdict(list)
    
    filelist = pd.DataFrame(columns=["checksum", "filename", "path", "size", "owner", "accesstime", "modifytime", "createtime"])
    #details structure is checksum, filename, path, size, owner, accesstime, modifytime, createtime
    
    file_types_inscope = ["ppt", "pptx", "pdf", "txt", "mp4", "html", "DAT", "jpg", "jpeg", "bmp", "doc", "docx", "xls", "xlsx"]

    # Walk through all files and folders within directory
    for path, dirs, files in os.walk(src_folder):
        #print("Analyzing {}".format(path))
        for each_file in files:
            if each_file.split(".")[-1].lower() in file_types_inscope:
                tmplist = []
                
                 # The path variable gets updated for each subfolder
                file_path = os.path.join(os.path.abspath(path), each_file)
                print( file_path)
                
                finfo=os.stat(file_path)
                #print( finfo)
                #print(type(finfo))
                md5_code = generate_md5(file_path)
                #if md5_code in filelist[:,0]:
                try:
                    tmplist = [generate_md5(file_path)]
                    tmplist.append(each_file)
                    tmplist.append(path)
                    tmplist.append(finfo[stat.ST_SIZE])
                    tmplist.append(finfo[stat.ST_UID])
                    tmplist.append(time.asctime(time.localtime(finfo[stat.ST_ATIME])))
                    tmplist.append(time.asctime(time.localtime(finfo[stat.ST_MTIME])))
                    tmplist.append(time.asctime(time.localtime(finfo[stat.ST_CTIME])))
                except:
                    print(file_path + " Error with file attributes")
                    pass
                #print(tmplist)
                filelist.loc[len(filelist)] = tmplist
                #filelist.append(tmplist)

    #print(filelist)
    # Write the list of duplicate files to csv file
    filelist.to_csv(src_folder +"/All_files.csv")
    
    dup_df = filelist[filelist.duplicated(subset=["checksum"], keep='first')].sort_values(by=["accesstime"])
    print(dup_df)
    dup_df.to_csv(src_folder +"/duplicates.csv")
    
    destination_folder = src_folder + "/temp"
    if not os.path.isdir(destination_folder):
        os.makedirs(destination_folder)
        print("created folder : ", destination_folder)

    for _, row in dup_df.iterrows():
        src_file = row.path + "/"+ row.filename
        print(src_file)
        try:
            shutil.move(src_file, destination_folder, copy_function='copy2')
        except:
                print(src_file+" already copied")
                pass
    
#     for dupPath, dupFile in dup_df['path'],dup_df['filename']:
#         print(dupFile)
       

    print("Done")