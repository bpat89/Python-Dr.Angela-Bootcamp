import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

all_names = len(names)
randomize = random.randint(0, all_names-1)
person = names[randomize]
print(f"lucky sponsor of today is {person}")
# Angela, Ben, Jenny, Michael, Chloe