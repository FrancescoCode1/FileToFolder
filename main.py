import os
from os import walk
import shutil

#creates a list of files ignoring folders
filenames = next(walk("Directory"), (None, None, []))[2]
original = r"directory"

#I don't know what I did here. It just worked so I didn't change it.
def main():
    #loops through the list
    for filename in filenames:
        #Making sure that it doesnt create a directory for directories
        if filename == os.path.isdir("directory"):
            pass
        #should have worked with switch case statements. When i wrote the code Python didnt feature switch-case. 
        #i have 2 file extensions. either mp4 or mkv. for either of those i want to create a directory and put them into the directory
        else:
            s = filename
            cutName = s.rfind(".mkv") #rfind returns -1 if the string is not in the filename

            if cutName > -1: 
                cutName = filename[:-4]  #this takes the filename and removes the last 4 symbols. Basically cuts the file extension
                dirName = (f"directory\\{cutName}") #stores the new name of the directory
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
