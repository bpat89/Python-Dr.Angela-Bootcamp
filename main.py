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
num2 = int(input("What's your second number? : \n"))
for symbol in operations:
    print(symbol)
operating_symbol = input("Pick a symbol from the lines above \n")

print(operations.(operating_symbol)(num1,num2))