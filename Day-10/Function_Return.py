# Formatting the Name


def name_format(f_name,l_name):
  formatted_f_name=f_name.title()
  formatted_l_name=l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"


f_name=input("Enter your First Name: ")
l_name=input("Enter your last name:")
formatted_name=name_format(f_name,l_name)
print(formatted_name)