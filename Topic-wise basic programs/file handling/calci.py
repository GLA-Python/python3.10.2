
import time
a = eval(input('Enter the first number '))
b = eval(input('Enter the second number '))
print('''
choices 
1. Addition
2. Subtraction
3. Division
4. Multiplication''')
choice = int(input('Enter the choice 1/2/3/4 '))
op = None
re = 0
if choice == 1:
    op = 'Addition'
    re = a + b
elif choice == 2:
    op = 'Subtraction'
    re = a - b
elif choice == 3:
    op = 'Division'
    re = a / b
elif choice == 4:
    op = 'Multiplication'
    re = a * b
else:
    print('Invalid Choice ')

st = f'{a}\t{b}\t{op}\t{re}\t{time.asctime()}\n'
f = open(r'C:\Users\drami\OneDrive\Desktop\section S\calci.txt', 'a')
f.write(st)
print(st)
f.close()
