import pilo

# simple variables are always passed by value
a = 1
b = a # by VALUE
a +=1
print(a, b)

# everything else is passed by ref
m = [8,7,6] 
n = m.copy() # no longer by reference
p = m # by REFERENCE
m[1] = 77

print(m,n)

# calling __main__
if __name__ == "__main__": # several things in Pyton use double underscores like this
    print('this is the main module')
