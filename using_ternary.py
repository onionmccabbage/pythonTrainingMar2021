# Python has one ternary operator
# i.e. an operator that takes THREE parts
# all other operators are binary, i.e. they take TWO parts
# e.g. a = 1 or 3+2

# the ternary operator works like this
# 'value if true' 'logical condition' 'value if false'

x = 6
y = 5
print("x" if x>y else "y")

# alternative syntax for the ternary operator
nice = False
personality = ("horrid", "lovely")[nice] # spot the index 0 or 1
print("My cat is {}".format(personality)) # 