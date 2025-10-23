# create a class 
class myClass:
    # private variable
    __privvar = 27;

    # private method
    def __privmeth(self):
        print("Im inside class myClass")

    # function to print value of private variable
    def hello(self):
        print("Private Var value: ",myClass.__privvar)

# object creation and method call
foo = myClass()
foo.hello()
foo.__privmeth()
