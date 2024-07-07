from zipfile import ZipFile
import os
import random
import concurrent.futures
import time

# Code Wrote by AaaaaaICO  ---> https://github.com/AaaaaaICO"

print("Made by AaaaaaICO")
print("Github ---> https://github.com/AaaaaaICO")
def GenerateHex(Length):
    possible = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hex = ""
    for i in range(Length):
        hex += possible[random.randint(0,len(possible)-1)]
    return hex

location = ""
newpath = ""
succeded = False
def RUN():

    def GetInputs():
        def Location():
            global location
            location = input("Where to extract from: ")
            if(os.path.isdir(location)):
                pass
            else:
                print("Could not find folder: " + location)
                Location()
        
        def FolderName():
            global newpath
            newFolderName = input("New folder name: ")
            newpath = location + "\\" + newFolderName
            if not os.path.exists(newpath):
                os.makedirs(newpath)
                print("\nCreated new folder: " + newpath)
            else:
                hex = GenerateHex(10)
                tempnewpath = location + "\\" "ZipExtractorByAaaaaaICO #" + hex
                print("\nThis folder already exists")
                print("[Y] add to the folder: " + newpath)
                print("[N] create a new folder: " + "ZipExtractorByAaaaaaICO #" + hex)
                CreateNewFolderYN = input("")
                if(CreateNewFolderYN == "Y" or CreateNewFolderYN == "y"):
                    print("Adding to folder: " + newpath)
                else:
                    newpath = tempnewpath
                    os.makedirs(newpath)
                    print("Created new folder: " + newpath)
        Location()
        FolderName()
    GetInputs()
    # loading the temp.zip and creating a zip object
    zipFolders = os.listdir(location)
    print("\nFound: " + str(len(zipFolders)) + " items in " + location)
    zipFoldersFound = 0
    for x in zipFolders:
        if(".zip" in x):
            zipFoldersFound += 1
    print("Found: " + str(zipFoldersFound) + " zipped folders in " + location)
    toDelete = input("[Y] Delete extracted zip folders\n[N] Keep extracted zip files\n")
    DeleteBool = False
    numFailed = 0
    if(toDelete == "Y" or toDelete == "y"):
        DeleteBool = True
    start_time = time.time()
    def ExtractZip(zipFolder):
        if ".zip" in zipFolder:
            print("\nExtracting zip file: " + zipFolder)
            zipLocation = location +"\\"+ zipFolder
            with ZipFile(zipLocation, 'r') as zObject:
                global succeded
                # Extracting all the members of the zip 
                # into a specific location.
                try:
                    zObject.extractall(path=newpath)
                    succeded = True
                    print("        Completed extracting zip file: " + zipFolder)
                except:
                    print("        Failed to extract zip file: " + zipFolder)
                    numFailed += 1
            if(succeded == True and DeleteBool == True ):
                try:
                    os.remove(zipLocation)
                    print("        Zip file deleted: " + zipFolder)
                except:
                    print("        Failed to delete zip file: " + zipFolder)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(ExtractZip, zipFolders)
                #ExtractZip(zipFolder)
    print("\n--- %s Seconds to finish---" % (time.time() - start_time))
    print(str(numFailed) + " zip files failed to be extracted")
    print("\nThank you for using this software")
    input("report any problems on the github page")

while True:
    RUN()