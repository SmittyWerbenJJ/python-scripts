from pathlib import Path
import subprocess
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

sevenzip=r"C:\Program Files\7-Zip\7zG.exe" # 7zg.exe for gui version | 7z.exe for console version

def extract(guid,files: list[str],callback):
    """
    Extract all files using 7zip in the same directory as the source files
    """
    if type(files) is not list:
        if type(files) is str:
            files=[files]
        else:
            raise RuntimeError("files must be a list of strings")
    file_length=len(files)
    progress=0
    callback({"id":guid,"status":"init","progress":progress,"total":file_length})

    #group the files so that we can extract multiple files in the same directory


    with ThreadPoolExecutor(max_workers=4) as executor:
        futures=[]
        allfiles=[]

        for file in files:
            parentDir=str(Path(file).with_suffix(""))
            cmd=f'{sevenzip} x "{file}" -o"{parentDir}" -y'
            future=executor.submit(subprocess.run,cmd,capture_output=True)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            progress+=1
            callback({"id":guid,"status":"progress","progress":progress,"total":file_length})

    callback({"id":guid,"status":"finished","progress":progress,"total":file_length})
