import os 
import shutil
source="Images"
dest="Test"
list_files=os.listdir(source)
for file in list_files:
    name,extension=os.path.splitext(file)
    if extension=='':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=source+'/'+file
        path2=dest+'/'+"Image_files"
        path3=dest+'/'+"Image_files"+'/'+file
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)