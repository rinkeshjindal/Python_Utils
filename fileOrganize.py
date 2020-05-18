import os 
from pathlib import Path 

DIRECTORIES = { 
	"HTML": [".html5", ".html", ".htm", ".xhtml"], 
	"IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
			".heif", ".psd"], 
	"VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
			".qt", ".mpg", ".mpeg", ".3gp"], 
	"DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
				".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
				".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsm", ".xlsx", ".ppt",
				"pptx"], 
	"ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
				".dmg", ".rar", ".xar", ".zip"], 
	"AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
	"PLAINTEXT": [".txt", ".in", ".out"], 
	"PDF": [".pdf"], 
	"PYTHON": [".py"], 
	"XML": [".xml"], 
	"EXE": [".exe"], 
	"SHELL": [".sh"] 

} 

FILE_FORMATS = {file_format: directory 
				for directory, file_formats in DIRECTORIES.items() 
				for file_format in file_formats} 

def organize_junk(scr_folder):
	for root, dirs, files in os.walk(scr_folder):
		# print("Analyzing {}".format(path))
		for each_file in files:
			print("file: "+each_file)
			file_path = os.path.join(root, each_file)
			file_format = file_path.split(".")[-1]
			if file_format in FILE_FORMATS:
				directory_path = os.path(FILE_FORMATS[file_format])
				directory_path.mkdir(exist_ok=True)
				file_path.rename(directory_path.joinpath(file_path))

		# for dir in os.scandir():
		# 	print("inside for: "+ dir)
		# 	try:
		# 		os.rmdir(dir)
		# 	except:
		# 		pass

if __name__ == "__main__": 
	organize_junk("D:/Online Data/temp")
