# create class
class Point:
    def __init__(self, y=0,x=0):
        self.y = y
        self.x = x

    def __str__(self):
        return "{0},{1}".format(self.y,self.x)
    
# create object
p1 = Point(2,3)
print(p1)