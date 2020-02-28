name =input('please enter name: ')
homework =int(input('enter homework <= 25: '))
asses =int(input('enter assessments <= 50: '))
exam =int(input('enter exam <= 100 : '))
def grade(name, homework, asses, exam):
    result = ((homework/25) + (asses/50) + (exam/100)) / 3
    print(name)
    return result*100
if grade(name, homework, asses, exam) >= 90:
    print('Excellent ', name ,', you scored an A')
elif grade(name, homework, asses, exam) >= 80:
    print ('Great job ', name ,', you scored a B')
elif grade(name, homework, asses, exam) >= 70 :
    print('good job ', name ,', you got a C')
elif grade(name, homework, asses, exam) >= 60 :
    print('nicely done ', name ,', you got a D')
else:
    print('Sorry ' ,name, ', you failed!')