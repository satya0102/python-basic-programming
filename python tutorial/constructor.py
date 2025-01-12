class student:
    def __init__ (self, Name , marks):
        self.name = Name
        self.marks = marks
        print("adding new student to database")

s1 = student("satya", 87)
print(s1.name, s1.marks) 
s2 = student("chandan", 88)
print(s2.name, s2.marks)


