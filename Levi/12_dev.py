# return statement: we cal=n call a python function, we want info from that function, like a particular value or how the task went
# the return keyword allows us to do that

# create a cube the number function

def cube(num):
    return num*num*num  # nothing can be put after the return statment, return keyword breaks us out of the function

result = cube(4)
print(result)