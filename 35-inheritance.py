#mechanism for using code
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

cat1 = Cat()
cat1.walk

#dog and cat classes inherit from their parent class
   

