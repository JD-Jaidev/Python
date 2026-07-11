# CLASS METHOD

class college:
    total = 0
    def __init__(self,name):
        self.name = name
        college.total += 1
    
    @classmethod
    def display_total(cls):
        print(f'Total number of students : {cls.total}') 

s1 = college('Jai')
s2 = college('Dev')
s3 = college('Thanish')

college.display_total()