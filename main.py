import os
from os import walk
import shutil

#creates a list of files without taking folders into consideration
filenames = next(walk("Directory"), (None, None, []))[2]
original = r"E:\Filme\__SMALL_FILES\Filme"

def main():
    #loops through the list
    for filename in filenames:
        #if the filename is a directory it wont create a directory
        if filename == os.path.isdir("E:\Filme\__SMALL_FILES\Filme"):
            pass

        else:
            s = filename
            cutName = s.rfind(".mkv")

            if cutName > -1:
                cutName = filename[:-4]
                dirName = (f"E:\Filme\__SMALL_FILES\Filme\\{cutName}")
                os.mkdir(dirName)
                shutil.move(original + f"\\" + s, dirName + f"\\" + s)

            elif cutName == -1:
                cutname = s.rfind(".mp4")
                if cutname > -1:
                    cutName = filename[:-4]
                    dirName = (f"E:\Filme\__SMALL_FILES\Filme\\{cutName}")
                    os.mkdir(dirName)
                    shutil.move(original + f"\\" + s, dirName + f"\\" + s)

                elif cutname == -1:
                    pass

if __name__ == "__main__":
    main()
