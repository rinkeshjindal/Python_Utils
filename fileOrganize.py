import os, sys
from pathlib import Path 
import shutil
from _ast import If

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

def organize_junk(scr_folder):
    for root, dirs, files in os.walk(scr_folder):
        # print("Analyzing {}".format(path))
        for each_file in files:
            #print("file: "+each_file)
            src_file = os.path.join(root, each_file)
            file_format = src_file.split(".")[-1].lower()
            p = Path(root)
            if file_format in FILE_FORMATS:
                f = FILE_FORMATS[file_format]
                cur_dir = root.rpartition('\\')[2]
                if cur_dir != f:
                    destination_folder = Path.joinpath(p, f)
                    destination_folder.mkdir(exist_ok=True)
                    shutil.move(src_file, destination_folder, copy_function='copy2')
                    print("moved: " + each_file)                    
                #file_path.rename(directory_path.joinpath(file_path))

        # for dir in os.scandir():
        #     print("inside for: "+ dir)
        #     try:
        #         os.rmdir(dir)
        #     except:
        #         pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # Print usage
        print("Usage: del_EmptyFilesFolders.py ""C:/Test""")
    else:
        src_path = sys.argv[1]
        
    organize_junk(src_path)
    print("Congrats, all files are organized in respective folders")
