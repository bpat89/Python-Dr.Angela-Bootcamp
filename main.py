# Instructions
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#   And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz

# if num is divisible by 3 print Fizz
# if num is divisible by 5 print Buzz
# if by both then FizzBuzz

# total = [0]
# for numbers in range(1,101):
#     total.append(numbers)
#     if numbers % 3 == 0 and numbers % 5 == 0:
#         total[numbers] = "FizzBuzz"
#     elif numbers % 3 == 0:
#         total[numbers] = "Fizz"
#     elif numbers % 5 == 0:
#         total[numbers] = "Buzz"
# print(total)

# Angela's way
for numbers in range(1,100):
    if numbers % 3 == 0 and numbers % 5 == 0:
        print("FizzBuzz")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)









