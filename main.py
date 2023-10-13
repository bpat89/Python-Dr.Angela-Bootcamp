# Calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
# created dictionary and stored in the variable named operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
num1 = int(input("What's your first number? : \n"))
for symbol in operations:
    print(symbol)
operating_symbol = input("Pick a symbol from the lines above \n")
num2 = int(input("What's your second number? : \n"))
# calling the function from the dictionary
operation = operations[operating_symbol]
# giving values for n1 and n2 to the callout function
first_answer = operation(num1,num2)
print(f"{num1} {operating_symbol} {num2} = {first_answer}")
operating_symbol = input("Pick a symbol from the lines above \n")
num3 = int(input("What's your second number? : \n"))
operation = operations[operating_symbol]
second_answer = operation(first_answer,num3)

print(second_answer)

print(f"{first_answer} {operating_symbol} {num3} = {second_answer}")






