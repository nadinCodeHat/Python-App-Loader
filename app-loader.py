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
    try:
        f = open("app-paths.txt")
    # Do something with the file
    except IOError:
        print("File not accessible")
    finally:
        f.close()

def add():

def update():

def remove():

def main():
    menu()

if __name__ == "__main__":
    main()