def moderate(marks, passMarks):
    if marks == passMarks -1 or marks == passMarks-2:
        marks = passMarks
    return marks

def main():
    passMarks = 40
    marks = input('enter marks: ')
    intMarks = int(marks)
    moderatedMarks = moderate(intMarks , passMarks)
    print('Moderated marks : ', moderatedMarks)


if __name__=='__main__':
    main()

