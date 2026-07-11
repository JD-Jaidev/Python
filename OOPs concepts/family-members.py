# MULTIPLE INHERITANCE

class father:
    def house(self):
        print('I live in dad house')

class mother:
    def kitchen(self):
        print('I use mom kitchen')

class son(father,mother):
    def factory(self):
        print('I go to my factory')

s = son()
s.house()
s.kitchen()
s.factory()
 
