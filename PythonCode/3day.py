#input
user_input = input()
print(user_input)


name = input("what's your name")
print("hello,"+name)

# This is a comment
'This is a string'
'This is a string'

#if
x = 1
if x == 1:
    print('x is 1')
    
# if and else
x = 2
if x == 1:
    print('x is 1')
else:
    print('x is not 1')
    
    
# if elif and else 
x = 0
if x > 0:
    print('x is positive')
elif x == 0:
    print('x is 0')
else:
    print('x is negative')
    
    
# Conditionals: try/except
#without use try and except
x = 10      # This value may come from user input
y = 'hello' # This value may come from user input
# result = y + x #error dont add the add deffernt veriable in one veriable
# print(result)

# using conditionals
x = 10      # This value may come from user input
y = 'hello' # This value may come from user input
try:
    result = y + x
except:
    result = 'wrong arguments'
print(result)

# Comparison Operators

m = 9
if(m==9):
    print("ok same")
else:
    print("ok not same")

# Functions
# def my_function():  # Function body...
# my_function() calling funciton

def my_function():
    print("Hello from a function")
    print("Bye from a function")
print("Hello from the main program")
my_function()
print("Bye from the main program")

def sum_two_numbers(a, b):
    print("The sum of", a, "and", b, "is", a + b)
print("Hello from the main program")
sum_two_numbers(5, 10)
print("Continuing the main program")
sum_two_numbers(15, 20)
print("Finishing the main program")

#last example
def sum_two_numbers(first_num, second_num):
    return first_num + second_num
print("The sum of 2 and 3 is", sum_two_numbers(2, 3))
