def calculator(num1,op,num2):
    if op == '+':
        return(num1 + num2)
    elif op == '-':
        return(num1 - num2)
    elif op == '*':
        return(num1 * num2)
    elif op == '/':
        if num2 != 0:
            return(num1 / num2)
        else:
            return("Error! Division by zero.")
    else:
        return("Invalid operator")
print(calculator(67,'+',2))
