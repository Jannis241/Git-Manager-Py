print("Welcome to Git Manager")
print("")
import os

path = os.path.dirname(os.getcwd())
files = os.listdir(path)
numOfFiles = len(files)


success = 0

commands = ["upload all", "update all", "download", "get username", "set username"]


def read_or_write_username(configPath):
    if not os.path.exists(configPath):
        with open(configPath, "w") as file:
            pass

    # Datei öffnen und prüfen, ob sie leer ist
    with open(configPath, "r+") as file:
        content = file.read().strip()

        if content:
            # Datei ist nicht leer, Username auslesen
            print(f"Benutzername: {content}")
            return content
        else:
            # Datei ist leer, nach Username fragen
            username = input("Bitte geben Sie Ihren Benutzernamen ein: ").strip()

            # Username in die Datei schreiben
            file.write(username)
            print(f"Benutzername '{username}' wurde in config.txt gespeichert.")
            print("")

            return username


configPath = os.path.join(os.getcwd(), "config.txt")
username = read_or_write_username(configPath)


print("> upload all / filename (commit message)")
print("> update all / filename")
print("> download repositoryName / https link")
print("> set username name")
print("> get username")
print("")


while True:
    inp = input("<Git> ")
    if inp == "get username":
        print("<Git> Username: " + username)

    if "set username" in inp:
        username = inp.split(" ")[2]
        with open(configPath, "w") as file:
            file.write(username)
            print(f"Benutzername wurde zu '{username}' geändert.")

    if "download" in inp:
        try:
            repoName = inp.split(" ")[1]
            os.chdir(path)
            if repoName.startswith("https://"):
                os.system(f"git clone " + repoName)

            else:
                os.system(f"git clone https://github.com/{username}/{repoName}.git")

        except:
            print("<ERROR> Repository or Username couldnt be found..")
        print("")
        print("")
    if inp == "update all":
        print("")
        print("Der Git-Manager wird durch 'update all' nicht beeinflusst..")
        print("")
        success = 0
        try:
            for file_name in files:
                if file_name and file_name != "Git-Manager":

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

            print(f"Updated {success}/{numOfFiles - 1} Projects successfully..")
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
        if input("<Confirm> Are you sure you want to upload all files to git? (y/n): ") == "y":
            print("")
            try:
                for file_name in files:
                    if file_name:
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
            splittedInput = inp.split(" ")

            file_name = inp.split(" ")[1]

            lenOfCommitMessage = len(splittedInput) - 2

            commitMessageList = splittedInput[-lenOfCommitMessage:]
            commitMessage = ""
            for word in commitMessageList:
                commitMessage += str(word) + " "

            newPath = path + "\\" + file_name
            if os.path.exists(newPath):
                os.chdir(newPath)
                os.system("git add .")
                os.system(f'git commit -m "{commitMessage}"')
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

    if not inp in commands and not "upload " in inp and not "update" in inp and not "download" in inp and not "set username" in inp:
        print(f'<ERROR> command "{inp}" not found.')
