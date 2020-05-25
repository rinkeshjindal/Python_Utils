import os, sys
import time
from pathlib import Path
import shutil
from shutil import Error
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

def organize_files(scr_folder, file_cat, target_folder):
    file_cat = file_cat.lower()
    for root, dirs, files in os.walk(scr_folder):
        for name in dirs:
            print(root+"/"+name)
            if file_cat in name.lower():
                src_dir = os.path.join(root, name)
                try:
                    shutil.move(src_dir, target_folder+"/"+name, copy_function='copy2')
                    print("moved: " + name)
                except:
                    print("unable to move dir: "+ name)
                    pass

        # print("Analyzing {}".format(path))
        for each_file in files:
            if file_cat in each_file.lower():
                print("file: "+each_file)
                src_file = os.path.join(root, each_file)
                file_format = each_file.split(".")[-1].lower()
                file_name = each_file.split(".")[0]

                create_time = os.path.getmtime(src_file)
                str_create_time = time.strftime("%Y%b%d", gmtime(create_time)) #Create Date Format

                if (str_create_time == file_name.rpartition('_')[2]):    #add date to filename if not already
                    new_file_name = each_file
                else:
                    new_file_name = file_name +"_" + str_create_time +"."+file_format

                p = Path(target_folder)
                if file_format in FILE_FORMATS:
                    f = FILE_FORMATS[file_format]
                    cur_dir = target_folder.rpartition('\\')[2]
                    if cur_dir != f: #check folder if already exists
                        destination_folder = Path.joinpath(p, f)
                        destination_folder.mkdir(exist_ok=True)
                    else:
                        destination_folder = target_folder

                    final_path = str(destination_folder) + "\\" + new_file_name

                    if src_file != final_path: #move / rename files
                            if Path(final_path).exists():
                                base_filename = new_file_name.split(".")[0]
                                ctr = 1
                                while(Path(final_path).exists()):
                                        new_file_name = base_filename + "_copy" + str(ctr)+ "." + file_format
                                        final_path = str(destination_folder) + "\\" + new_file_name
                                        ctr = ctr + 1
                            shutil.move(src_file, final_path, copy_function='copy2')
                            print('moved file')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        # Print usage
        print("Usage: del_EmptyFilesFolders.py ""C:/Test""")
    else:
        src_path = sys.argv[1]
        file_cat = sys.argv[2]
        target_folder = sys.argv[3]
    organize_files(src_path, file_cat, target_folder)
    print("Congrats, all files are organized in respective folders")
