# String

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

print("Full Name:", full_name)

print("Data_Type: " + str(type(full_name)))

print(type(first_name)) # to check the type of a variable use function type()
print(type(first_name) == str) # this will return True if first_name is of type string
print(type(last_name),str) # this will return the type of last_name and the string class

#Casting number to string
age = 30
age_str = str(age) # this will convert the integer age to a string

# concatenation of string
year = 1980
print(type(year)) # this will return the type of year which is int
year_str = str(year) # this will convert the integer year to a string
statement = "I love the music of the " + year_str + "s"
print(statement)


# multi-line string
multiline_string = '''
I am learning python programming.
It's a great language for data science and web developement.  

Everyone should learn it!
                                    Thanks, KD

'''
print(multiline_string)

# escaping special characters in string. "\n is used to create a new line, \" is used to include double quotes in the string, and \' is used to include single quotes in the string.
escaped_string = "I\'m a Python developer, \"Python is awesome!. \n\nI am located in \"Singapore\"."
print(escaped_string)

# String Methods
name = "Alice"
print(name.upper()) # this will convert the string to uppercase
print(name.lower()) # this will convert the string to lowercase
print(name.capitalize()) # this will convert the first character to uppercase and the rest to lowercase
print(name.replace("A", "E")) # this will replace all occurrences of "A" with "E"
print(name)
print(len(name)) # this will return the length of the string

# String concatenation and formatting
sentence = "My name is" + " " + name + " and I am learning Python."
sentence += " It's a great language for programming."
print(sentence)
sentence = "                                    Join me soon!                                    "
print(sentence)
print(sentence.strip()) # this will remove the leading and trailing whitespace from the string
print(sentence.rstrip()) # this will remove the trailing whitespace from the string
sentence.center(50) # this will center the string within a field of width 30
print(sentence)

# ==========================================
# Coffee House Menu String Formatting
# ==========================================
title = "Welcome to KD's Coffee House".upper()
print(title.center(50, "-"))

# FIXED: Moved closing parentheses to the very end of the print statement
print("Coffee".ljust(20, ".") + "$2.50".rjust(10)) 
print("Tea".ljust(20, ".") + "$2.00".rjust(10))
print("Pastry".ljust(20, ".") + "$3.30".rjust(10))