from zipfile import ZipFile
import os
import random
import concurrent.futures
import time
from threading import Thread
import sys
# Code Wrote by AaaaaaICO  ---> https://github.com/AaaaaaICO"


FilesFinished = 0
WriteQueue = []
WriteQueueUpdate = False
RUNNING = True
def RunningCheck():
    global RUNNING
    global WriteQueueUpdate
    while True:
        if(RUNNING):
            time.sleep(5)
            print("--Running--")

def GenerateHex(Length):
    possible = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hex = ""
    for i in range(Length):
        hex += possible[random.randint(0,len(possible)-1)]
    return hex

def ExtractZipFiles(FromLocation, ToLocation, NewFolderName, DeleteOldFile):
    RunningCheckThread = Thread(target = RunningCheck)
    RunningCheckThread.start()


    ZipFilesFound = 0
    FilesFound = 0
    NumExtractsFailed = 0
    StartTime = time.time()

    FolderToWriteTo = ToLocation
    if(NewFolderName != ""):
        FolderToWriteTo += "//" + NewFolderName

    def CreateNewFolder(Name, Location):
        if(os.path.isdir(Location)):
            if(Name == ""): # Dont create a folder if no name is specified
                pass
            else:
                try:
                    os.makedirs(Location + "//" + Name)
                except:
                    print(("--ERROR-- assuming folder already exists: " + Location + "//" + Name))
        else:
            print("--ERROR-- ToLocation doesnt exist")
            return "ERROR"

    def ExtractZipFile(zipFile):
        global ZipFoldersFound
        if(".zip" in zipFile):
            global WriteQueueUpdate
            WriteQueue.append("Found: " + zipFile)
            WriteQueueUpdate = True
            ZipLocation = FromLocation +"\\"+ zipFile
            with ZipFile(ZipLocation, "r") as zObject:
                try:
                    zObject.extractall(path=FolderToWriteTo)
                except:
                    NumExtractsFailed += 1
            if(DeleteOldFile == True):
                try:
                    os.remove(ZipLocation)
                except:
                    pass
            else:
                pass
    # Verify FromLocation exists
    if(os.path.isdir(FromLocation)):
        errorcheck = CreateNewFolder(NewFolderName, ToLocation)
        if(errorcheck == "ERROR"):
            return "ERROR"
    else:
        print("--ERROR-- FromLocation doesnt exist")
        return "ERROR"

    zipFolders = os.listdir(FromLocation) # gets all files inside FromLocation
    for x in zipFolders:
        FilesFound += 1
        if(".zip" in x):
            ZipFilesFound += 1
    print("Files found: " + str(FilesFound))
    print("Zip files found: " + str(ZipFilesFound) + "\n")
    with concurrent.futures.ThreadPoolExecutor() as executor: # concurrently extracts zip files
        executor.map(ExtractZipFile, zipFolders)
    print("\n--- %s Seconds to finish ---" % (time.time() - StartTime))
    print(str(NumExtractsFailed) + " zip files failed to be extracted")
    print("\nThank you for using this software")
    print("report any problems on the github page")
    global WriteQueueUpdate
    WriteQueueUpdate = True
    global RUNNING
    RUNNING = False
    RunningCheckThread.join()

args = sys.argv
ExtractZipFiles(args[1], args[2], args[3], args[4])