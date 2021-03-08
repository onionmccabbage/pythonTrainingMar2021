# exploring lists, tuples, sets and dict collections

l = [7,6,5,4] # a mutable list!
l[1] = 6.5
l.append(99)
l.insert(2,88)
print(l[0:])
lt = tuple(l)
print(lt)
t = (7,) # an immutable tuple
print(t)

# non-indexed collections
d = {'name':'Ada', 'age':42, 'member':True} # keys MUST be string or number
d['nums'] = l
print(d, d['name'], type(d))

# Careful there is no reliable default order to the members of a set or dict

# a set
s = {4,3,2,1} # memers of a set MUST be unique
s2 = {'wobble', 'weeble', 'wibble'} # data types of a set MUST all be the same
s3 = {t, t, t}
print(s.add(5)) # add(4) will not add since 4 already exists
print(s, type(s), s2)
# accessing members of a set
for item in s2: # nb no brackets
    print(item)
for item in d:
    print(item, d[item])
# range, generator and comprehension
exist = 'wubble' in s2
print(exist)
for i in range(0, 10, 3): # a bit like for (i; i<10; i++){}
    print('hello {}'.format(i))

for i in range(0, len(l)):
    print(l[i])

# range is a generator object
my_values = ( num for num in range(-10**100, 10**100) ) # a tuple generator object
print(my_values)

for i in my_values:
    pass
    # print(i)