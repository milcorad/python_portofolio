
import os
import sys
from os import listdir
import os.path
import datetime
import shutil

# Get the args of the running script
path = str(sys.argv[1])

# File/Directory functions
def move_file():
    filename = input("Filename: ")
    to_path = input("Set the path to be moved: ")
    global path
    shutil.copy(path+"/"+filename, to_path)
    print("File moved successful")


def change_path():
    global path
    print(f'{path} is the current path')
    path = input("Enter the new path: ")
    print(f"Path changed to: {path}")

# Create directory function
def create_dir():
    folder_name = input("Enter he folder name: ")
    cpath  = os.path.join(path, folder_name)
    os.mkdir(cpath, 0o555)
    return True
 # Create txt file function
def create_file():
    file_name = input("Enter filename: ")
    with open(os.path.join(path, file_name), "w") as b:
        print(f"\n \n File {file_name} created successful \n \n ")

# Delete directory
def delete_dir():
    dir_path = input("Enter folder name: ")
    os.rmdir(path+dir_path )

# Delete files, any type
def delete_file():
    filename = input("Enter the filename to be deleted: ")
    if os.path.exists(path+filename):
        os.remove(path+filename)
    else:
        print("Filename don't exist")

# Change directory, forward or back like cd in cmd
def change_directory():
    directory = input("' .. ' for back, dir name to change the current dir >> ")
    global path 
    if directory == "..":
        path = path.split("/")
        path.pop()
        path.pop()
        path = "/".join(path) + "/"        
    else:
        path = path.split("/")
        path.pop()
        path.append(directory)
        path = "/".join(path)+"/"
        
    print("Current path: ", path)
# Print Working Dirs
def pwd():
    global path
    if os.path.exists(path):
        print("Path exist")
    else:
        print("Wrong path")

    print(f"Current path: {path}")
    print(" \n \n Cr. Date \t  Type \t \t  Name")
    print("_"*60)
    c = list([j for j in listdir(path)])
    for j in c:
        path1 = str(path+j)
        try:
            #try to get the creation date
            creation_date = datetime.datetime.fromtimestamp(os.path.getmtime(path1))
            creation_date = creation_date.date()
        except FileNotFoundError:
            creation_date = "unknown"
        else:   
            # Format the string output
            print(creation_date, "\t", " File  \t" if os.path.isfile(path+j) else " Dirs  \t",f'{j :<25}'  )
    print("_"*60)

# Print the .txt file content 
def read_file():
    filename = str(input(" Filename to open: >> "))
    file =  open (path+"/"+filename, "r")
    content = file.read()
    print(content)
    file.close()



if __name__ == "__main__":
    # Main loop
    while True:
        print("\n \n1 - List dir")
        print("2 - Create dir ")
        print("3 - Delete dir")
        print("4 - Create file")
        print("5 - Delete file")
        print("6 - Change Directory")
        print("7 - Read .txt file")
        print("8 - Move file")
        print("0 - Exit")
        option = int(input(">> "))

        match option:
            case 1:
                pwd()
            case 2:
                create_dir()
            case 3:
                delete_dir()
            case 4:
                create_file()
            case 5:
                delete_file()
            case 6:
                change_directory()
            case 7:
                read_file()
            case 8:
                move_file()
            case 0:
                sys.exit(0)