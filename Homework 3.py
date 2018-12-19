Var1 = 5
Var2 = 8
Var3 = 11

def CompareVars2(num1, num2, num3) :
    
    
    if int(num1) == int(num2) or int(num1) == int(num3) or int(num2) == int(num3):
        message = "At least two numbers are equal"
        return message
    else:
        message = "None of the parameters are equal"
        return message

result = CompareVars2(Var1, Var2, Var3)
print(result)

Num1 = 2
Num2 = 3
Num3 = "3"

result = CompareVars2(Num1, Num2, Num3)
print(result)