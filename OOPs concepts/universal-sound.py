# POLYMORPHISM AND DUCK TYPING

class dog:
    def sound(self):
        print('Dog barks...')

class cat:
    def sound(self):
        print('Cat meows...')

class cow:
    def sound(self):
        print('Cow moos...')

def make_sound(animal):
    animal.sound()

animals = [dog(),cat(),cow()]

for animal in animals:
    make_sound(animal)