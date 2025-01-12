#create student class that take name and marks of 3 subjects as argument in constructor then create a method to priint the average 

class student:
    def __init__(self , name ,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is: ", sum/3)
s1 = student("satya singh", [98,88,77])
s1.get_avg()



