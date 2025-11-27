class Students:
    """
    An empty class representing a students.
    The 'pass' keyword is used to fill the empty block.
    """
    pass

# Instance of the empty class
s1 = Students()

"""
 Adding Attributes to class Dynamically 
you can add attributes to a specific instance later
"""
s1.name = "Archita"
s1.age = 19
s1.city = "Pune"

print(f"{s1.name} lives in {s1.city}.")

# Instance s2 can have completely different attributes
s2 = Students()
s2.id = 123
s2.email = "myemail@gmail.com"

print(s1.name, s1.city) # Output: Archita Pune
print(s2.id, s2.email)   # Output: 123 myemail@gmail.com
