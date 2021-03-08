# exploring Python functions
import math # the math library is not a default part of Python but it IS a default library

def addNums(x=0, y=0): # we can provide default values
    z = x+y
    return z

# pythagorus
def pythag(x=3, y=4):
    """
    This is a docstring - your chance to explain the purpose of the function
    Arguments for x and y are received
    and the hypotenuse of a r-a triangle is returned
    """
    # hyp = (x*x + y*y)**0.5 # power of 0.5 is the square root
    # or
    hyp = math.sqrt(x*x + y*y)
    return hyp

# the arguments of a function can be accessed by position or by keyword
def usingArgs(*args): # the * indicates we want the positional arguments
    print(args) # ANY positional arguments will be gatehred into the 'args' tuple

# mini challenge - sum all numeric arguments passed in to a function
def sumNumbers(*args): # we expect zero or more positional arguments
    if len(args) == 0:
        pass # the zero-argument version of this funtions
    elif len(args) == 1:
        pass        
    total = 0
    for item in args:
        if type(item)==float or type(item)==int: # there is also an 'and' operator
            total += item
    return total

# We can also access the keyword arguents using **kwargs
# for example we might need a name, age and a list of roles (all strings)
def makeUser(**kwargs): # Python will gather zero or more keyword arguments into a dict
    print(kwargs)
    for key, value in kwargs.items(): # .items() returns the tuples, .value() returns the value 
        print(key,value)

# immediate code
result = addNums(y=4) # invoke the function
result = addNums(5, 6) # the arguments are positional, i.e. 0, 1, ..
print(result)
help(pythag)
result = pythag(y=-4, x=-3) # invoke with keyword arguments returns 5
print(result)
usingArgs(False, 'wooobly', [5,4,3], 42)
print( sumNumbers(True, 3, 4, 5.3, 'nope', '1.2') ) # 12.3
makeUser(name='Timnit', age=879, roles=[])
