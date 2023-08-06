# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print( "Good Morning ")
#     print("Today is a Clear day for victory")
#     print("universe is in my favor all the time")
# greet()
newName = input("Please enter your name : ")
def greet_with_name (name):
    print( f"Good Morning {name}")
    print(f"Today is a Clear day for victory")
    print(f"universe is in my favor all the time")
greet_with_name(newName)
