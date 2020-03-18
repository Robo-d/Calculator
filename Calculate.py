from function import *

while True:
    print("What do u want to do")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("Enter Q or q to Exit")

    choice = input("Enter your choice : ")

    if choice == 'Q' or choice == 'q':
        break

    num1 = float(input("Enter Number 1 : "))
    num2 = float(input("Enter Number 2 : "))

    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
        multiplication(num1.num2)
    elif choice == '4':
        division(num1,num2)
    else:
        print("Invalid choice")