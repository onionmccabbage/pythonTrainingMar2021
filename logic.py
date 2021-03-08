a = 1.2345678900000000009
b = 2.3456
print(repr(a))



a = input('First number? ')
b = input('Second number? ')
# Pythin is happy with single or double quotes 
if (a<b):
    print( '{0} is less than {1}'.format(a,b) )
elif (a>b): # not else if
    print( '{} is greater than {}'.format(a,b) )
else:
    print('other')
# end of block - no more indentation
