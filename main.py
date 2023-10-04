def formated_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "you didn't provide a valid input"
  formated_fname = f_name.title()
  formated_lname = l_name.title()
  return f"{formated_fname} {formated_lname}"

print(formated_name(input("Please enter your first name: "),input("Please enter your last name: ")))
