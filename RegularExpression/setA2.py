"""program using regex to find sequences of lowercase letters joined with an underscore.
lowercase_letters + underscore + lowercase_letters
^[a-z]+_[a-z]+$
[a-z]+ → one or more lowercase letters
_ → underscore
$ → end of string
^ → start of string
"""

import re
text = input("Enter a string: ")
pattern = r'^[a-z]+_[a-z]+$'

if re.fullmatch(pattern, text):
    print("Valid: Matches the pattern lowercase + underscore + lowercase")
else:
    print("Invalid: Does not match the required pattern")
