import os
from os import walk
import shutil

filenames = next(walk(r"C:\\Users\\Example"), (None, None, []))[2]
original = r"C:\\Users\\Example"

#checkFiletype: stores the value of rfind. if filetype exists it returns > -1 otherwise -1


def main():
    for filename in filenames:
        if filename == os.path.isdir("directory"):
            pass
        else:
            s = filename
            checkFiletype = s.rfind(".mkv")
            
            if checkFiletype > -1:
                filenameNoExt = filename[:-4]
                dirName = (f"C:\\Users\\Example\\{filenameNoExt}")
                os.mkdir(dirName)
                shutil.move(original + f"\\" + s, dirName)
            elif checkFiletype == -1:
                mp4name = s.rfind(".mp4")
                
                if mp4name > -1:
                    filenameNoExt = filename[:-4]
                    dirName = (f"C:\\Users\\Example\\{filenameNoExt}")
                    os.mkdir(dirName)
                    shutil.move(original + f"\\" + s, dirName)
                elif mp4name == -1:
                    pass
                
if __name__ == "__main__":
    main()
