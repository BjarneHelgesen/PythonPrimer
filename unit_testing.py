'''
name = input("Type your name ")
firstName, lastName = name.split(" ", 2)
print("My name is", lastName, firstName, lastName)
'''

def unit_test():
    assert doMath(1, "+", 2) == 3
    assert doMath(1, "-", 2) == -1
    assert doMath(1, "*", 2) == 2
    assert doMath(1, "/", 2) == 0.5
    assert doMath(1, "x", 2) == "Invalid operator"
    print("All tests passed")

def doMath(number1, operator, number2):
    if operator == "+":
        return number1 + number2
    if operator == "-":
        return number1 - number2
    if operator == "*":
        return number1 * number2
    if operator == "/":
        return number1 / number2

    return "Invalid operator"
    
unit_test()
math_expression = input("Type a math expression: ")
number1, operator, number2 = math_expression.split()
result = doMath(int(number1), operator, int(number2))
print(math_expression, "=", result) 

