# we can import our other classes
import using_classes_a as a
# we can declare a class that inherist from some other class
class Coder(a.Person): # we inherit everything the Person class defined
    '''
    Explain your class in a docstring like this
    This class inherits all the peoperties and methods of the Person class
    then adds a 'language' property
    We also override the original showMe method with a new one
    '''
    def __init__(self, name, email, age, language):
        super().__init__(name, email, age) # we call the parent class constructor
        self.__language = language
    # we need a better 'showMe' method
    def showMe(self): # remember all methodds of a class MUST take self as an argument
        print('Name is {} email is {} age is {} lang is {}'.format(self.name, self.email, self.age, self.__language))
    # we can override built-in methods such as __str__
    def __str__(self):
        return 'This is my own version of the __str__ method'


if __name__ == '__main__':
    fred = a.Person('Timnit', 't@g.ie', 39)
    ada = Coder('Ada', 'ada@babbage.ie', 99, 'Ada')
    ada.showMe()
    # we can access the documentation
    print(ada.__doc__, ada) # when we print stuff, Python uses the __str__ operator