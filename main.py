# Functions with Outputs

def format_names(f_name, l_name):
    conv_fname = f_name.title()
    conv_lname = l_name.title()
    return f"{conv_fname} {conv_lname}"
full_string = format_names("universe", "is always creative")
print(full_string)
