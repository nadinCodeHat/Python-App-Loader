import os
from fileinput import filename

def menu():
    while True:
        print("########## Python App loader ##########")
        print("1: Run all Apps")
        print("2: Add App")
        print("3: Read App paths")
        print("4: Exit")
        print("#######################################")
        choice=int(input("Enter your choice : "))
        if choice == 1:
            run()
        elif choice == 2:
            add()
        elif choice == 3:
            read()
        elif choice == 4:
            quit()
        else:
            print("Invalid Input")
            menu()

def run():
    if os.path.isfile('app-paths'):
        if os.path.getsize('app-paths') > 0:
            count = 0
            with open("app-paths") as file_read:
                while True:
                    count += 1
                    line = file_read.readline()
            
                    if not line:
                        break
                    os.startfile(line.strip())
                    print("Running : "+line.strip())
        else: print ("File empty!")
    else: print("File not exist")

def add():
    app_path=(input("Add app path : "))
    if os.path.isfile("app-paths"):
        with open("app-paths", "a+") as file_append:
            file_append.seek(0)
            data = file_append.read(100)
            if len(data) > 0 :
                file_append.write("\n")
            file_append.write(app_path)
    else:
        with open("app-paths","w+") as file_write:
            file_write.write(app_path)
    print("Path Added!")

def read():
    count = 0
    with open("app-paths") as file_read:
        while True:
            count += 1
            line = file_read.readline()
    
            if not line:
                break
            print("{}: {}".format(count, line.strip()))

def main():
    menu()

if __name__ == "__main__":
    main()