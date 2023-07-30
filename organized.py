import os
import shutil 

from_dir = "/Users/jain_rishu80/Downloads/C102_assets-main" 
to_dir = "/Users/jain_rishu80/Desktop/C_102"
list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension == "":
        continue
    if extension in[".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        path1 = from_dir + "/"+ file_name
        path2 = to_dir + "/" + "Image_Files"
        path3 = to_dir + "/" + "Image_Files" + "/" + file_name
        
    if os.path.exists(path2):
        print("moving" + file_name + "...")
        shutil.move(path1, path3)

    else:
        os.makedirs(path2)
        print("moving" + file_name + "...")
        shutil.move(path1, path3)