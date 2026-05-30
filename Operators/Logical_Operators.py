'''Logical Operators

These are used to combine multiple conditional statements. 
They also return True or False.
- and: Returns True only if both statements are true.
--- (5 > 3) and (10 > 5) $\rightarrow$ True
--- (5 > 3) and (10 < 5) $\rightarrow$ False

- or: Returns True if at least one of the statements is true.
--- (5 > 3) or (10 < 5) $\rightarrow$ True

- not: Reverses the result (turns True to False, and vice versa).
--- not(5 > 3) $\rightarrow$ False

'''

a = 5
b = 10
c = 7
d = 6

ans1 = ( a > b) and (c > d)
ans2 = ( a > b) or (c > d)
print(ans1)
print(ans2)


num1 = 15
num2 = 17
if(num1 < num2):
    print("num1 is smaller than num2")
else:
    print("num1 is not smaller than num2")
    
# ternary operator
print("num1 is greater than num2") if (num1 > num2) else print("num1 is not greater than num2")
