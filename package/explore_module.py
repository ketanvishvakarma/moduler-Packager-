def main():
    while True:
        print("select an option")
        print("1. For math operations")
        print("2. For random data generation")
        print("3. For UUID generation")
        print("4. For datetime and time operations")
        print("5. For file operations")
        print("6. For Back to main menu")

        choice= input("enter your choice: ")

        if choice == 1:
            import math
            print(dir(math))

        elif choice ==2:
            import random
            print(dir(random))

        elif choice==3:
            import uuid
            print(dir(uuid))

        elif choice==4:
            import datetime
            print(dir(datetime))

        elif choice==5:
            import file_utils_module
            print(dir(file_utils_module))

        elif choice==6:
            break   

