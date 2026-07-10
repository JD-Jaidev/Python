class student:
    count = 0
    def __init__(self,name):
        self.name = name
        student.count += 1

s1 = student('Jai')
s2 = student('Dev')
s3 = student('Thanish')

print('total students : ',student.count)

