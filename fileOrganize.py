import os, sys
import time
from pathlib import Path
import shutil
from _ast import If
from time import gmtime

DIRECTORIES = { 
    "HTML": ["html5", "html", "htm", "xhtml"], 
    "IMAGES": ["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg", 
            "heif", "psd"], 
    "VIDEOS": ["avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng", 
            "qt", "mpg", "mpeg", "3gp"], 
    "DOCUMENTS": ["oxps", "epub", "pages", "docx", "doc", "fdf", "ods", "csv",
                "odt", "pwi", "xsn", "xps", "dotx", "docm", "dox", 
                "rvg", "rtf", "rtfd", "wpd", "xls", "xlsm", "xlsx", "xltx", "ppt",
                "pptx"], 
    "ARCHIVES": ["a", "ar", "cpio", "iso", "tar", "gz", "rz", "7z", 
                "dmg", "rar", "xar", "zip"], 
    "AUDIO": ["aac", "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3", 
            "msv", "ogg", "oga", "raw", "vox", "wav", "wma"], 
    "PLAINTEXT": ["txt", "in", "out"], 
    "PDF": ["pdf"], 
    "PYTHON": ["py"], 
    "XML": ["xml"], 
    "EXE": ["exe"], 
    "SHELL": ["sh"] 

} 

FILE_FORMATS = {file_format: directory 
                for directory, file_formats in DIRECTORIES.items() 
                for file_format in file_formats} 

def organize_files(scr_folder):
    for root, dirs, files in os.walk(scr_folder):
        # print("Analyzing {}".format(path))
        for each_file in files:
            #print("file: "+each_file)
            src_file = os.path.join(root, each_file)
            file_format = each_file.split(".")[-1].lower()
            file_name = each_file.split(".")[0]

            create_time = os.path.getctime(src_file)
            str_create_time = time.strftime("%Y%b%d", gmtime(create_time)) #Create Date Format
            
            if (str_create_time == file_name.rpartition('_')[2]):    #add date to filename if not already
                new_file_name = each_file
            else:
                new_file_name = file_name +"_" + str_create_time +"."+file_format
            
            p = Path(root)
            if file_format in FILE_FORMATS:
                f = FILE_FORMATS[file_format]
                cur_dir = root.rpartition('\\')[2]
                if cur_dir != f: #check folder if already exists
                    destination_folder = Path.joinpath(p, f)
                    destination_folder.mkdir(exist_ok=True)
                else:
                    destination_folder = root
                
                destination_folder = str(destination_folder) + "\\" + new_file_name

                if src_file != destination_folder: #move / rename files
                    shutil.move(src_file, destination_folder, copy_function='copy2')
                    print("moved: " + each_file)                    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # Print usage
        print("Usage: del_EmptyFilesFolders.py ""C:/Test""")
    else:
        src_path = sys.argv[1]
        
    organize_files(src_path)
    print("Congrats, all files are organized in respective folders")
