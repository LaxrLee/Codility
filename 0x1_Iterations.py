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

# Example: We are given some positive integer n. Let's compute the factorial of n and assign it to the variable factorial. The factorial of n is n! = 1 . 2 ... n
#  We can obtain it by starting with 1 and multiplying it by all the integers from 1 to n

factorial = 1
for i in range(1, n + 1):
    factorial *=1


# Let's print a triangle made of asteriks(*). The trianglke should consist of n rows, where n is a given positive integer, and consecutive rows should contain 1,2,...n
# in asteriks. for example , for n = 4 
# We need to use two loops, one inside the other: the outer loop should print one row in each stepo and the inner loop should print one asterix in each step.

for i in range(1, n+1):
    for j in range(i):
        print ('*'),
    print