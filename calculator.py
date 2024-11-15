print(" _____________________")
print("|  _________________  |")
print("| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------.")
print("| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |")
print("|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |")
print("| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |")
print("| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |")
print("| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |")
print("| |___|___|___| |___| | | |  \\ '.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ '.___.'\\  | |")
print("| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |")
print("| |___|___|___| |___| | | |              | || |              | || |              | || |              | |")
print("| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |")
print("| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'")
def new_cal():
    first_num = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    user_func = input("Pick an operation: ")
    second_num = float(input("What's the next number?: "))

    if user_func == "+":
        result = first_num + second_num
        print(f"{first_num} + {second_num} = {result}")
    elif user_func == "-":
        result = first_num - second_num
        print(f"{first_num} - {second_num} = {result}")
    elif user_func == "*":
        result = first_num * second_num
        print(f"{first_num} * {second_num} = {result}")
    elif user_func == "/":
        if second_num != 0:
            result = first_num / second_num
            print(f"{first_num} / {second_num} = {result}")
        else:
            print("Error! Division by zero is not allowed")
            return  
        return  
    
    return result

def calculator():
    result=new_cal() 

    while True:
        user_decision = input("Type 'yes' to continue calculating with the result, or 'no' to start a new calculation,and exit: ").lower()
        
        if user_decision == "no":
            result=new_cal() 
        elif user_decision == "yes":
            operation = input("+\n-\n*\n/\nPick an operation : ")
            second_num = float(input("What's the next number?: "))
            
            if operation == "+":
                result += second_num
                print(f"Result: {result}")
            elif operation == "-":
                result -= second_num
                print(f"Result : {result}")
            elif operation == "*":
                result *= second_num
                print(f"Result : {result}")
            elif operation == "/":
                if second_num != 0:
                    result /= second_num
                    print(f"Result: {result}")
                else:
                    print("Error! Division by zero is not allowed")
            else:
                print("Invalid operation")
        elif user_decision=="exit":
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            

calculator()