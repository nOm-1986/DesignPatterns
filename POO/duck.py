"If it looks like a duck and quacks like a duck, then it must be a duck"

def make_it_quack(duck):
    duck.quack()

class Duck:
    def quack(self):
        print("Quack!!!")

class Dog:
    def barck(self):
        print("Woof!!!")

d = Duck()
make_it_quack(d) # This prints "Quack!!!"

dog = Dog()
# make_it_quack(dog) # This fails because Dog