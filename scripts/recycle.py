# import send2trash
# import os
# from pathlib import Path
# import winutils
# import pythoncom
# from win32cm.shell import shell,shellcon
# def recycle(filepaths):
#     """Move files to recycle bin"""
#     dirs=[]
#     files=[]
#     for filepath in filepaths:
#         if os.path.isdir(filepath):
#             dirs.append(filepath)
#         else:
#             files.append(filepath)
#     winutils.delete(files,)


# with open(Path(__file__).parent.joinpath("filelist.txt"),"r",encoding="utf8") as file:
#     for line in file:
#         path =Path( line.strip())
#         try:
#             send2trash.send2trash(path)
#             print("deleted",path)
#         except FileNotFoundError:
#             pass
