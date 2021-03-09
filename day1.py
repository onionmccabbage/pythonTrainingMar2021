# there are four general ways to store data
# first, in a scalar containing ONE value
a = 1
b = True
# second in an indexed collection, accessible via zero-based index values [start:stop:step]
l = [9,8,7] # any data type is permitted for the data members
t = (6,5,4) # we say these are ordinal ie 0, 1, 2 ,3 ...
s = 'an indexed collection of characters'
# third in a mutable collection of name:value pairs 
# nb name can be anything but usually a quoted string
d = {'id':42, 'user':'Ethel', 'email':'ehtel@skronk.ie'}
d['email'] = 'new@other.ie'
print(d)

# if it's just simple data, then single values are fine
# if we need to relate data, then use a collection (or a class)
# if the order of the data matters, then use an INDEXED collection ie list or tuple
# if the ordinal members need to be mutated, use a list
# if there is no natural order to the data members then use a dictionary

# and lastly as classes (see later)

# we can store ANY data type in any other data structure
my_t = ('Mon', 'Tue', 'Wed', [] )

# we can gather together other collections into a dictionary
collect = {'user':d, 'days':my_t, 'geo':{'lat':52, 'lon':0} }

# we can access any member of a collection
print(collect['user']['email']) # new@other.ie
print(collect['days'][1]) # 'Tue'
