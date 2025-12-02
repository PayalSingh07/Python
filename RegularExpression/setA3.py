import re

def check_string(string, allowed_chars):
    # Create regex pattern using only allowed characters
    #pattern = r'^[' + allowed_chars + r']+$'
        
    #pattern = rf"^[{allowed_chars}]+$"
    pattern = rf"^[{allowed_chars}]+"

    # Check if the entire string matches allowed characters
    if re.fullmatch(pattern, string):
        return True
    else:
        return False


# Example usage
allowed = "abc123"    # define allowed characters
text = "ab1c23abc231bca"        # test string

if check_string(text, allowed):
    print("Valid string: contains only allowed characters.")
else:
    print("Invalid string: contains characters outside allowed set.")

allowed = input("Enter Allowed Characters : ")
text = input("Enter the String : ")

if check_string(text, allowed):
    print("Valid string: contains only allowed characters.")
else:
    print("Invalid string: contains characters outside allowed set.")
