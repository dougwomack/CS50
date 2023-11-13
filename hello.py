# Ask user for their name
name = input("What's your name? ")

# Strip whitespace and title case name
name = name.strip().title()

# Split first name and last name
first, last = name.split(" ")

# Say hello to user
print ("Hello " + first)
print ("Hello " + first, last, end=" :-)\n")
print (f"Hello {first} {last}")