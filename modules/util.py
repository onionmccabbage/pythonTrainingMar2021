# this is util.py
# it will contain utilities we might need
def checkInt(i):
    # check i is an int
    if type(i) == int:
        return i
    else:
        try:
            i = int(float(i))
        except Exception:
            i = 0
        finally:
            return i

if __name__ == '__main__':
    # the following lines will ONLY run if
    # we run this module as the main module
    # When we import to other modules, this code
    # will NOT run
    print(checkInt(3))      # expect 3
    print(checkInt(3.4))    # expect 3
    print(checkInt('3'))    # expect 3
    print(checkInt('oops')) # expect 0