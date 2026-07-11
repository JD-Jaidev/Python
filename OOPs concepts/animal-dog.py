class animal:
    def eat(self):
        print('Dog eats bone')

class dog(animal):
    def sound(self):
        print('Dog barks')

d = dog()
d.eat()
d.sound()