import time 
a = eval(input('Enter the first number '))
b = eval(input('Enter the second number '))

print('''
choices 
1> Add
2> Subtract
3> Division
4> Multiply

''')

choice = int(input('Enter the choice 1/2/3/4 '))

op = None
re = 0


if choice == 1:
    print('User choice Addition')
    op = 'Addition'
    re = a + b
elif choice == 2:
    print('User choice Subtraction')
    op = 'Subtract'
    re = a - b
elif choice == 3:
    print('User choice Division')
    op = 'Division'
    re = a / b
elif choice == 4:
    print('User choice Multiplication')
    op = 'Multiply'
    re = a * b
else:
    print('Invalid Choice, Try Again ')


st = f'{a}\t{b}\t{op}\t{re}\t{time.asctime()}\n'

with open(r'C:\Users\drami\OneDrive\Desktop\section J\calc.txt', 'a+') as f:
    f.write(st)
    

