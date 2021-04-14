import os.path
from fileinput import filename

def menu():
        print("1: Run all Apps")
        print("2: Add App")
        print("3: Update App")    
        print("4: Remove App")
        choice=int(input("Enter your choice:"))
        if choice == 1:
            run()
        elif choice == 2:
            add()
        elif choice == 3:
            update()
        elif choice == 4:
            remove()
        else:
            print("Invalid Input")
            menu()


def run():
    if os.path.isfile('app-paths.txt'):
        if os.path.getsize('app-paths.txt') > 0:
            print ("File exist and not empty")
            f = open("app-paths.txt")
        print ("File empty!")
    print("File not exist")

def add():
    app_path=(input("Add app path : "))
    exists = False
    if os.path.isfile('app-paths.txt'):
        exists = True
    else:
        exists = False
    
        with open(filename, "app-paths.text")
def update():

def remove():

def main():
    menu()

if __name__ == "__main__":
    main()