#to define new types to model new concept #P is called pascal naming convention
#no _ to separate multiple words, we capitalize the letter
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

#after we define .1, we can have attributes anywhere in out programs