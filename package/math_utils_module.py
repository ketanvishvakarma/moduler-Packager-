from datetime import datetime
import time
import math
from uuid import uuid4 

def dt_operations():
    while True:
        print()
        print("Datetime and Time Operations: ")
        print("Display current date and time")
        print("Calculate difference between two dates/times")
        print("Format date into custom format")
        print("Stopwatch")
        print("Countdown Timer")
        print("Back to main Menu")

        choice=int(input("Enter your choice "))

        if choice==1:
            print(f"Current Date and Time :{datetime.now()}")

        elif choice==2:
            dt1=input("Enter the First Date (YYYY-MM-DD) :")
            dt2=input("Enter the Second Date (YYYY-MM-DD) :")

            dt1= datetime.strptime( "%Y-%m-%d",dt1)
            dt2= datetime.strptime( "%Y-%m-%d",dt2)
            
            print(f"Difference: {abs(dt2-dt1)}")

        elif choice==3:
            print("select an option")
            print("1. For Date")
            print("2. For Time")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                current_date=datetime.now()
                print(current_date.strftime("%Y-%m-%d"))

            elif choice ==2:
                current_time=datetime.now()
                print(current_time.strftime("%H:%M:%S"))

            else:
                break

        elif choice ==4:

            start=time.time()
            input("press enter to stop")
            stop=time.time()
            print(f"Your time is : {stop-start}")

        elif choice ==5:
            n=int(input("Enter the time in seconds for countdown: "))
            while n>0:
                print(n)
                time.sleep(1)
                n-=1
            print("Countdown finished!")

        elif choice==6:
            break

def math_operations():
    while True:
        print()
        print("Mathematical Operations: ")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. trigonometric calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice=int(input("Enter your choice "))

        if choice==1:
            n=int(input("Enter a number to calculate factorial: "))
            print(f"Factorial of {n} is {math.factorial(n)}")

        elif choice==2:
            money= int(input("Enter your money"))
            year=int(input("Enter your year"))
            rate=int(input("Enter your rate"))
            cp=money*(1+(rate/100))**year
            print(f"Compound Interest is {cp}")

        elif choice==3:
            pass

def uuid():
    id=uuid4()
    print(f"UUID: {id}")