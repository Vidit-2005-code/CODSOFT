def calculator():
    
    print("Calculator")
    print("-"*40)
    
    try:
        operator = input("Enter operation(+,-,*,/): ")
        num_1 = float(input("Enter first Number: "))
        num_2 = float(input("Enter second number: "))

        if operator == "+":
            result = num_1 + num_2
            print(f"{result:.2f}")
        elif operator == "-":
            result = num_1 - num_2
            print(f"{result:.2f}")
        elif operator == "*":
            result = num_1 * num_2
            print(f"{result:.2f}")
        elif operator == "/":
            if num_2 == 0:
                print("Not Defined")
            else:
                result = num_1 / num_2
                print(f"{result:.2f}")
        else:
            print("Invalid Operator")

    except:
        print("Invalid Numeric Value")

    print("-"*40)
    
calculator()