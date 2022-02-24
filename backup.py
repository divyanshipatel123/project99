import os
import time

path = input("Enter the directory path: ")

#Getting time
now = time.time()
day = 30*24*60*60
Ourtime = now  - day

#Getting cTime
def getctime(path):
    ctime = os.stat(path).st_ctime
    return ctime

if os.path.exists(path):

    for root , dir , files in os.walk(path):
  
        if Ourtime >= getctime(root) :
            os.remove(root)
            print("The directory "+ str(root) + "has been deleted for bieng older than 30 days")
            break

        else:
            for folder in dir :
                subFolder = os.path.join(root , folder) 

                if Ourtime >=  getctime(subFolder) :
                    os.remove(subFolder)
                    print("The directory "+ str(subFolder)+ " has been deleted for bieng older than 30 days")

            for file in files:
                filePath  = os.path.join(root , file)

                if now >= getctime(filePath):
                    os.remove(filePath)
                    print("The file "+ str(filePath)+ " has been deleted for bieng older than 30 days")   
                    
else:
    print("please enter valid directory path")