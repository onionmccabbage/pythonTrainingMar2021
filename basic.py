# here is a comment
a = 3 # integer
b = 7
c = a/b
# fun with maths
# + = / *
d = b//a # returns the integer part of division
e = b**a
f = b%a # remainder after division
print(d, e, f)
print(type(c), type(a))
# dealing with large numbers
# g = 10**100000
# print(g)

# strings are immutable collections of characters
s = 'Timnit'
print(s[0:5:2]) # start:stop-before:step
print(s[::-1])
# we CANNOT alter members of a string
# s[0] = 't' # TypeError: 'str' object does not support item assignment
s = True # False note tha capital letter
n = input('enter a number ')
print(type(n))
m = int( float(n) )
print(type(m))