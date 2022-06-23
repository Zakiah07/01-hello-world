class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11 #if want to add a new value
print(point.x)

#constructor is a function that get called at the time of creating an object