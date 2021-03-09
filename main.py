# this is main.py

# we can import our own modules into this module
# import my_module as m
from my_module import makeCube as make
# import modules.util
from modules.util import checkInt

def main():
    num = input('which number? ')
    # num = modules.util.checkInt(num)
    num = checkInt(num)
    # c = m.makeCube(3) # expect 27
    c = make(num) # we imported this one function and called it 'make'
    print(c)

if __name__ == '__main__':
    main()