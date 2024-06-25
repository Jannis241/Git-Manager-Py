print("Welcome to Git Manager")
print("")
 
print("> upload all / filename")
print("> update all / filename")
print("> download webUrl")
print("")

import os
path = os.getcwd()

files = os.listdir(path)
numOfFiles = len(files) - 1
success = 0

commands = ["upload all", "update all", "download"]

while True:
    inp = input("<Git> ")

    
    if "download" in inp:
        try:
            repoName = inp.split(" ")[1]
            os.system("git clone " + repoName)
            print(f"<Status> Download {repoName}: success")

        except:
            print("<ERROR> Something went wrong..")
        print("")
        print("")
    if inp == "update all":
        print("")
        success = 0
        try:
            for file_name in files:
                if file_name != "git.py":

                    if file_name.lower() == "q":
                        exit()

                    newPath = path + "\\" + file_name

                    if os.path.exists(newPath):
                        os.chdir(newPath)
                        os.system("git pull origin main")
                        print(f"<Status> {file_name}: success")
                        success += 1
                        print("")
                        print("")
                    else:
                        print(f"File '{file_name}' does not exist in the current directory.")
                        print(f"<Status> {file_name}: failed")
                        print("")
                        print("")

                    
            print(f"Updated {success}/{numOfFiles} Projects successfully..")
        except:
            print("<ERROR> Update failed..")

        print("")
        print("")

    elif "update" in inp:
        
        try:
            file_name = inp.split(" ")[1]
            newPath = path + "\\" + file_name
            if os.path.exists(newPath):
                os.chdir(newPath)
                os.system("git pull origin main")
                print(f"<Status> {file_name}: success")
                print("")
                print(f"Updated {file_name} successfully..")
            else:
                print(f"File '{file_name}' does not exist in the current directory.")
                print(f"<Status> {file_name}: failed")
        except:
            print("<ERROR> Update failed..")
            
            
        print("")
        print("")

    if inp == "upload all":
            success = 0
            if input ("<Confirm> Are you sure you want to upload all files to git? (y/n): ") == "y":
                print("")
                try:
                    for file_name in files:
                        if file_name != "git.py":
                            newPath = path + "\\" + file_name

                            if os.path.exists(newPath):
                                os.chdir(newPath)
                                os.system("git add .")
                                os.system('git commit -m "automatic python commit"')
                                os.system("git push origin main")
                                print(f"<Status> {file_name}: success")
                                success += 1
                                print("")
                                print("")
                            else:
                                print(f"File '{file_name}' does not exist in the current directory.")
                                print(f"<Status> {file_name}: failed")
                                print("")
                                print("")

                            
                    print(f"Uploaded {success}/{numOfFiles} Projects successfully..")
                except:
                    print("<ERROR> Upload failed..")
                
                print("")
                print("")




    elif "upload" in inp:
        
        try:
            file_name = inp.split(" ")[1]
            newPath = path + "\\" + file_name
            if os.path.exists(newPath):
                os.chdir(newPath)
                os.system("git add .")
                os.system('git commit -m "automatic python commit"')
                os.system("git push origin main")
                print(f"<Status> {file_name}: success")
                print("")
                print(f"Uploaded {file_name} successfully..")
            else:
                print(f"File '{file_name}' does not exist in the current directory.")
                print(f"<Status> {file_name}: failed")
        except:
                print("<ERROR> Upload failed..")
        
        
        print("")
        print("")


    if inp == "q" or inp == "quit":
        exit()

    if not inp in commands and not "upload " in inp and not "update" in inp and not "download" in inp:
        print(f'<ERROR> command "{inp}" not found.')
