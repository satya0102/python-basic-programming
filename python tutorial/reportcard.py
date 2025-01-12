def assignGrade(marks):
    assert marks >= 0 and marks <=100 
    if marks >= 90:
       grade = 'A+'
    elif marks >= 70:
        grade = 'A'
    elif marks >= 60:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    elif marks >= 40:
        grade = 'D'
    else:
        grade = 'fail'
    return grade

def main():

    marks= float(input('Enter your marks: ')) 
    print('Marks:', marks , '\n grade: ', assignGrade(marks))

if __name__ == '__main__':
        main()



