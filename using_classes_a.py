# classes let us formalize cutom data structures

class Person(): # implicitly, our class inherits from the Object class in Python
    # the __init__ method MUST alsways take self as an argument
    def __init__(self, name, email, age): # this is like a constructor (but optional)
        self.__name = name # these are properties of the class
        # we can protect the properties by using __
        self.__email = email # the double underscore convention is called 'name mangling'
        self.age = age # this is accessible directly from outside the class
    # we can declare methods  of this class
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age = age

    def showMe(self): # all class methods MUST take self as an argument
        print('Name is {} email is {} age is {}'.format(self.__name, self.__email, self.age))
    # we can write accessor and mutator methods (aka getter and setter) for properties
    @property # this is a built-in decorator
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if name !='' and type(name) == str:
            self.__name = name
        else:
            self.__name = 'NA'

    @property # this is a built-in decorator
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        if email !='' and type(email) == str:
            self.__email = email
        else:
            self.__email = 'NA'


if __name__ == '__main__':
    # we can create instances of our class
    fred = Person('Fred', 'f@e.ie', 42)
    ada = Person('Ada', 'a@babbage.ie', 89)
    fred.name = True # this fails silently
    fred.email = 'new@me.ie' #  alters the email property of the class instance via the @email.setter method
    fred.set_age(99)
    fred.age = -99 # oops!!
    fred.showMe()
    ada.showMe()