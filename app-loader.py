import os.path
from fileinput import filename

def menu():
        print("1: Run all Apps")
        print("2: Add App")
        print("3: Update App")    
        print("4: Remove App")
        print("5: Exit")
        choice=int(input("Enter your choice : "))
        if choice == 1:
            run()
        elif choice == 2:
            add()
        #elif choice == 3:
            #update()
        #elif choice == 4:
            #remove()
        #elif choice == 5:
            #quit()
        else:
            print("Invalid Input")
            menu()

def run():
    if os.path.isfile('app-paths'):
        if os.path.getsize('app-paths') > 0:
            print ("File exist and not empty")
            f = open("app-paths")
        print ("File empty!")
    print("File not exist")

def add():
    app_path=(input("Add app path : "))
    if os.path.isfile("app-paths"):
        with open("app-paths", "a+") as file_append:
            # Move read cursor to the start of file.
            file_append.seek(0)
            # If file is not empty then append '\n'
            data = file_append.read(100)
            if len(data) > 0 :
                file_append.write("\n")
            # Append text at the end of file
            file_append.write(app_path)
    else:
        f= open("app-paths","w+")
        f.write(app_path)
    

#def update():

#def remove():

def main():
    menu()

if __name__ == "__main__":
    main()