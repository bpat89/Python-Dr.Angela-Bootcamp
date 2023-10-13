# calculator



def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operating_symbols = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = int(input("please enter you first number \n"))
    for symbols in operating_symbols:
        print(symbols)
    to_continue = True
    while to_continue:
        operation = input("please select the operator \n ")
        num2 = int(input("please enter the next number \n"))
        function = operating_symbols[operation]
        answer = function(num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")
        if input("would you like to continue type 'y' for yes and 'n' to exit ") == "y":
            num1 = answer
        else:
            to_continue = False
            calculator()

calculator()










