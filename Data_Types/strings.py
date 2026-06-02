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