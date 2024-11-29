import os
import shutil
current_dir = os.getcwd()
for file in os.listdir(current_dir):
    if file == "organizer.py" or file == "index.html":
        continue
    else:
        file_extension = file.split(".")[1]
        if os.path.exists(f"./{file_extension}"):
            shutil.copy(f"./{file}", f"./{file_extension}")
            os.remove(file)
        else:
            os.makedirs(f"./{file_extension}")
            shutil.copy(f"./{file}", f"./{file_extension}")
            os.remove(file)