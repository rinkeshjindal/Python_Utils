import os, sys
import time
from pathlib import Path
import shutil
from shutil import Error
from _ast import If
from time import gmtime
from json.decoder import NaN

DIRECTORIES = {
    "HTML": ["html5", "html", "htm", "xhtml"], 
    "IMAGES": ["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg", 
            "heif", "psd"], 
    "VIDEOS": ["avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng", 
            "qt", "mpg", "mpeg", "3gp"], 
    "DOCUMENTS": ["oxps", "epub", "pages", "docx", "doc", "fdf", "ods", "csv",
                "odt", "pwi", "xsn", "xps", "dotx", "docm", "dox", 
                "rvg", "rtf", "rtfd", "wpd", "xls", "xlsm", "xlsx", "xltx", "ppt",
                "pptx","prn"],
    "ARCHIVES": ["a", "ar", "cpio", "iso", "tar", "gz", "rz", "7z", 
                "dmg", "rar", "xar", "zip"], 
    "AUDIO": ["aac", "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3", 
            "msv", "ogg", "oga", "raw", "vox", "wav", "wma"], 
    "PLAINTEXT": ["txt", "in", "out"], 
    "PDF": ["pdf"], 
    "PYTHON": ["py"], 
    "XML": ["xml"], 
    "EXE": ["exe"], 
    "SHELL": ["sh"],
    "Tax": ["T14","T15","T16","T17","T18","T19","T20"]
} 

FILE_FORMATS = {file_format: directory 
                for directory, file_formats in DIRECTORIES.items() 
                for file_format in file_formats} 


folder = {'Visa': ['visa','797'], 
          'passport': ['passport'],
          'Alisha': ['Alisha', 'jiya'],
          'Pooja': ['Pooja', 'rimpy'],
          'Sharvil': ['Sharvil'],
          'resume': ['resume', 'it_prof'],
          'education': ['education', 'MCA', 'Graduation'],
          'finance': ['tax', 'statement_', 'savings', 'mortgage'],
          'salary': ['salary', 'payslip','paycheck']
          }

def search(values, file_name):
    for k in values:
        #print(file_name.lower())
        for v in values[k]:
            #print("v: " + v.lower())
            if v.lower() in file_name.lower():
                return k
    return None

def organize_files(scr_folder, target_folder):
    for root, dirs, files in os.walk(scr_folder):
        for name in dirs:
            #print(root+"/"+name)
            cat_folder = search(folder, name)
            if cat_folder != None:
                src_dir = os.path.join(root, name)
                p = Path(target_folder)
                if target_folder.rpartition('\\')[2] != cat_folder:  # check folder if already exists
                    destination_folder = Path.joinpath(p, cat_folder)
                    destination_folder.mkdir(exist_ok=True)
                    print("Created folder: "+str(destination_folder))
                else:
                    destination_folder = target_folder
                #p = Path(destination_folder)
                try:
                    shutil.move(src_dir, str(destination_folder)+"/"+name, copy_function='copy2')
                    print("moved: " + name)
                except:
                    print("unable to move dir: "+ src_dir + " to " +target_folder+"/"+cat_folder+"/"+name)
                    #raise
                    pass

        #print("root: " + root)
        for each_file in files:
            cat_folder = search(folder, each_file)
            if cat_folder != None:
                src_file = os.path.join(root, each_file)
                file_format = each_file.split(".")[-1].lower()
                file_name = each_file.split(".")[0]
                #print("file: " + each_file)
                if file_format in FILE_FORMATS:
                    create_time = os.path.getmtime(src_file)
                    str_create_time = time.strftime("%Y%b%d", gmtime(create_time)) #Create Date Format

                    if (str_create_time == file_name.rpartition('_')[2]):    #add date to filename if not already
                        new_file_name = each_file
                    else:
                        new_file_name = file_name +"_" + str_create_time +"."+file_format
                    #print("target_folder: " + str(target_folder))
                    p = Path(target_folder)
                    if target_folder.rpartition('\\')[2] != cat_folder: #check category folder if already exists
                        destination_folder = Path.joinpath(p, cat_folder)
                        destination_folder.mkdir(exist_ok=True)
                    else:
                        destination_folder = target_folder
                    #print("destination_folder: "+str(file_format))
                    p = Path(str(destination_folder))

                    f = FILE_FORMATS[file_format]
                    cur_dir = str(destination_folder).rpartition('\\')[2]
                    if cur_dir != f: #check fileFormat folder if already exists
                        destination_folder = Path.joinpath(p, f)
                        destination_folder.mkdir(exist_ok=True)
                    else:
                        destination_folder = destination_folder
                    #print("before Final_folder: " + str(destination_folder))
                    final_path = str(destination_folder) + "\\" + new_file_name
                    #print("final_path: "+str(final_path))
                    if src_file != final_path: #move / rename files
                        if Path(final_path).exists():
                            base_filename = new_file_name.split(".")[0]
                            ctr = 1
                            while(Path(final_path).exists()):
                                new_file_name = base_filename + "_copy" + str(ctr)+ "." + file_format
                                final_path = str(destination_folder) + "\\" + new_file_name
                                ctr = ctr + 1
                        shutil.move(src_file, final_path, copy_function='copy2')
                        print('moved file' + src_file +" to "+ final_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        # Print usage
        print("Usage: del_EmptyFilesFolders.py ""C:/Test""")
    else:
        src_path = sys.argv[1]
        target_folder = sys.argv[2]
    organize_files(src_path, target_folder)
    print("Congrats, all files are organized in respective folders")
