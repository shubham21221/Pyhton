# Loops
# while loop
x = 5
while x > 0:
    print("the value of x is:", x)
    x = x - 1

# Output:
# the value of n is: 5
# the value of n is: 4
# the value of n is: 3
# the value of n is: 2
# the value of n is: 1

x = 5
while x > 0:
    print("the value of x is:", x)
    if x == 2:
        print("exiting loop - the value of x has reached", x)
        break
    x = x - 1

# Output
# the value of x is: 5
# the value of x is: 4
# the value of x is: 3
# the value of x is: 2
# exiting loop - the value of x has reached 2

x = 5
while x > 0:
    modifier = 1
    x = x - modifier
    print("the value of x is:", x + modifier)
    if (x + modifier) % 2 != 0:
        continue
    print("    and this is an even value")

# Output:
# the value of x is: 5
# the value of x is: 4
#     and this is an even value
# the value of x is: 3
# the value of x is: 2
#     and this is an even value
# the value of x is: 1


# for loop

array = [5, 4, 3, 2, 1]
iteration = 0

for i in array:
    print("The iteration", iteration, "returns the element", i)
    iteration = iteration + 1

# Output
# The iteration 0 returns the element 5
# The iteration 1 returns the element 4
# The iteration 2 returns the element 3
# The iteration 3 returns the element 2
# The iteration 4 returns the element 1