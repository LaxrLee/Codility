# Iterating means repeating some part of your program. This lesson represents basic programming constructions that allow iterations to be performed: "for"
# and "while"

# 1.1 For Loops - repeat an peration a given number of time
# for some_variable in range_of_values:
#     loop_body

# In its simplest form, the range of values can be a range of integers, range(lowewst, highest + 1)

for i in range(0, 100):
    print (i)

# looping over a range of integers starting from 0 is a very common operation(Mainly because arrays and python lists are indexed by integers starting from 0;)
# If it starts with zero you can skio it. Its is similar to this:

for i in range (100):
    print(i)

# Example: We are given some positive integer n. Let's compute the factorial of n and assign it to the variable factorial. 
# The factorial of n is n! = 1 . 2 ... n
#  We can obtain it by starting with 1 and multiplying it by all the integers from 1 to n

factorial = 1
for i in range(1, n + 1):
    factorial *=1


# Let's print a triangle made of asteriks(*). The trianglke should consist of n rows, where n is a given positive integer, 
# and consecutive rows should contain 1,2,...n
# in asteriks. for example , for n = 4 
# We need to use two loops, one inside the other: the outer loop should print one row in each stepo and the inner loop should print one asterix in each step.

for i in range(1, n+1):
    for j in range(i):
        print ('*'),
    print 

# Print a triangle made of asteriks seperated y spaces and consisting of n rows again, but this time upside down, and make it symetrical. 
# Consecutive rows should contain 2n - 1, 2n - 3, ..., 3, 1 asteriks should be indented by 0, 2, 4, ..., 2(n-1) spaces.
# the triangle should have n rows, where n is some given positive integer. 
# this time we use three loops: one outer and two inner loops. The outer loop in each step prints one row of the triangle. 
# The first inner loop is responsible for printing the asteriks.

for i in range(n, 0, -1):
    for j in range(n - i):
        print (' '),
    for j in range(2 * i - 1):
        print (' * '),
    print