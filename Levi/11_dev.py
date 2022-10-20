# functions - a collection of code that perform a specific task

# function to say hello

def hello():
    print("Hello User")

# code inside a function is only executed when we spoecify that we want it executed
# hello()

# with functions ewe will need additional information to pass in. These are called parameters
# a parameter is a piece of information that we give to the function

def say_hi(name):
    print ("Hello " + name)   #name is the parameter

say_hi(input("Enter name: "))
