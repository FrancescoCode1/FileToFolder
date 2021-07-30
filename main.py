import os
from os import walk
import shutil

#creates a list of files ignoring folders
filenames = next(walk("Directory"), (None, None, []))[2]
original = r"directory"

def main():
    #loops through the list
    for filename in filenames:
        #if the filename is a directory it wont create a directory
        if filename == os.path.isdir("directory"):
            pass

        else:
            s = filename
            cutName = s.rfind(".mkv")

            if cutName > -1:
                cutName = filename[:-4]
                dirName = (f"directory\\{cutName}")
                os.mkdir(dirName)
                shutil.move(original + f"\\" + s, dirName + f"\\" + s)

            elif cutName == -1:
                cutname = s.rfind(".mp4")
                if cutname > -1:
                    cutName = filename[:-4]
                    dirName = (f"directory\\{cutName}")
                    os.mkdir(dirName)
                    shutil.move(original + f"\\" + s, dirName + f"\\" + s)

                elif cutname == -1:
                    pass

if __name__ == "__main__":
    main()
