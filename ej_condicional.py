import random
#Ejercicios para condicionales
'''1.1 Ask the user to input a number (should be integer). Check if the number is even or odd. Remember that 0 is neither even nor odd.


1.2 Ask the user to input a number (should be integer). Check whether the number is zero, positive or negative.


1.3 A school has following grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 60 - D
d. 60 to 75 - C
e. 75 to 90 - B
f. Above 90 - A
Ask user to enter marks (assuming the marks are between 0 and 100) and print the corresponding grade.
'''
#1.1
n =int(input(' introduce un numero. '))
if n == 0:
    print('para el numero 0, no se puede decir que es impar o par.')
elif n % 2 ==0:
    print('es un numero par. ')
else:
    print('Es un numero impar. ')

#1.2
n1 = int(input('Introduce un numero entero: '))
if n1 ==0:
    print('el numero elegido es cero. ')
elif n1<0:
    print('El numero escogido es negativo. ')
elif n1>0:
    print('es un numero positivo. ')

#1.3
x = int(input(' Introduce tu calificacion(recuerda que tiene que estar entre 0-100): '))
if x <25:
    print('Tu calificacion es una F. ')
elif 25 <= x <45:
    print('Tu calificacion es una E. ')
elif 45 <= x < 60:
    print('Tu calificacion es una D. ')
elif 60 <= x < 75:
    print('Tu calificacion es una C. ')
elif 75 <= x < 90:
    print('Tu calificacion es una B. ')
elif x >= 90:
    print('Tu calificacion es una A. ')

if x <50:
    print('Tienes que estudiar mas has suspendido. ')
elif 50<= x <70:
    print('estas aprobado sigue estudiando')
else:
    print('felicidades crack cacho nota loco.')