import os
from pathlib import Path
import subprocess
import tempfile
from PIL import Image
import csv
import io

"""
THis script will find all folders that only contain image files
"""
# root_dir = Path(r"C:\Users\smitty\Desktop\sort")

# #get all image suffixes recognized by pillow
# pillow_image_suffixes=[f".{x[1:].lower()}" for x in Image.registered_extensions()]

# # walk root directory and create a list of subfolders that only include images
# image_only_folders = []


# for root, dirs, files in os.walk(root_dir):
#     #skip directory if it only contains folders
#     if len(dirs) > 0 and len(files) == 0:
#         continue

#     # check if all files inside are images
#     all_images = True
#     for filename in files:
#         if Path(filename).suffix.lower() not in pillow_image_suffixes:
#             all_images = False
#             break

#     # if all files in directory are images, add directory to list
#     if all_images:
#         image_only_folders.append(root)

# with (tempfile.NamedTemporaryFile("w",delete=False,suffix=".efu")) as file:
#     fieldnames=["Filename","Size","Date Modified","Date Created","Attributes"]
#     writer = csv.DictWriter(file,fieldnames)
#     writer.writeheader()
#     for folder in image_only_folders:
#         writer.writerow({
#             "Filename":f'{folder}',
#             "Size":os.path.getsize(folder),
#             "Date Modified":int(os.path.getmtime(folder)),
#             "Date Created":int(os.path.getctime(folder)),
#             "Attributes":os.stat(folder).st_file_attributes
#         })

# #run the file. this will open everything with the results
# os.startfile(file.name)
