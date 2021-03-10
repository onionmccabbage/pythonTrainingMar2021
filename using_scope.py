# every module has it's own scope
# all code blocks also have their own scope
# we try not to pollute the global scope

meta = 'this is a global variable'

def method():
    global meta # we now hve access to the global variable called meta, within this block
    meta = 'this is scoped to the current code block'
    return meta

print(meta)
print(method())
print(meta)
