#Creating a simple calculator which perfroms actions like addition, substraction, multiplication and division

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a/b
    else:
        return "Error! Cannot divide by Zero."
    

def calculator():
    while(True):
        print("Choose which action you want to perform.")
        print("1.Addition \n2.Substraction\n3.Multiplication \n4.Division \n5.Exit\n")
        
        try:
            choice = int(input("Choose any one option: "))
        except ValueError:
            print("Invalid input! Please enter a number (1–5).")
            continue
        
        if choice == 5:
            print("Closing Calculator, Bye")
            break
        
        if choice in [1, 2, 3, 4]:
            try:
                num1 = float(input("Enter num 1 : "))
                num2 = float(input("Enter num 2 : "))
            except ValueError:
                print("invalid choie, choose between 1-5")
                continue
            
            if choice == 1:
                print("Result : ", addition(num1, num2))
            elif choice == 2:
                print("Result : ", substraction(num1, num2))
            elif choice == 3:
                print("Result : ", multiplication(num1, num2))
            elif choice == 4:
                print("Result : ", division(num1, num2))
        else:
            print("Enter valid choice.")
           
calculator()        
    
    

    
            