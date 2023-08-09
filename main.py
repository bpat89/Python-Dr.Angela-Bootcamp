programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}
# Retrieving the dictionary.
# print(programming_dictionary["Bug"])
# Adding new items to the dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating an empty dictionary.
empty_dictionary = {}
# Wipe an existing dictionary.
# programming_dictionary = {}
# print(programming_dictionary)
# Edit an item in a dictionary
# programming_dictionary["Bug"] = "some new information"
# print(programming_dictionary)
# Looping throught the dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
