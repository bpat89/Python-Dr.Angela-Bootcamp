def format_name(f_name, l_name):
    """ Takes the first and last name and converts into title case version of the name"""
    if f_name == "" or l_name == "":
        return "You didn't provide a value"
    format_fname = f_name.title()
    format_lname = l_name.title()
    return f"{format_fname} {format_lname}"

print(format_name(input("First Name : "), input("Last Name: ")))

"""" Now if you call the function format_name(),
 as soon as you bring the arrow into the parenthesis you will see the description of the function""""


























