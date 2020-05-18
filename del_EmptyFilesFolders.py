
#-------------------------------------------------------------
#    del_EmptyFilesFolders.py
#    Deletes all empty folders under a given path.
#    
#    Created on May 11, 2020
#
# author: Rinkesh_Jindal
#
#    Usage: del_EmptyFilesFolders.py "C:/Test"
#-------------------------------------------------------------

import sys, os

ctr_dir = 0
ctr_files = 0

if len(sys.argv) == 1:
    # Print usage
    print("Usage: del_EmptyFilesFolders.py ""C:/Test""")
else:
    for root, dirs, files in os.walk(sys.argv[1], topdown=False):
        for name in dirs:
            try:
                if len(os.listdir( os.path.join(root, name) )) == 0: #check if the directory is empty
                    print( "Deleting", os.path.join(root, name) )
                    try:
                        os.rmdir( os.path.join(root, name) ) #Delete Empty Folder
                        ctr_dir = ctr_dir + 1
                    except:
                        print( "FAILED :", os.path.join(root, name) )
                        pass
            except:
                pass
        
        for f in files:
            try:
                full_name = os.path.join(root, f)
                if os.path.getsize(full_name) == 0:
                    print( "Deleting", full_name  )
                    try:
                        os.remove(full_name)    #Delete Empty File
                        ctr_files = ctr_files + 1
                    except:
                        print( "FAILED :", full_name )
                        pass
            except:
                pass
    print("dir removed: "+ str(ctr_dir))
    print("Files removed: " + str(ctr_files))