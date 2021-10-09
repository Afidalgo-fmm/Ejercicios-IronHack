#Ejercicios
'''

Write a simple for loop to print integers from 10 to 30. Also write a code to print those numbers in steps of 3.


1.2 Update the previous code to print all the numbers from 10 to 30 that are multiples of 5.


1.3 Write a code to print this pattern. Modify the print statement in the dummy code provided

'''
#1.1

for i in range(10,30):
    print(i)

for i in range(10,30,3):
    print(i)

#1.2

for i in range(10,30):
    if i % 5 ==0:
        print(i)

#1.3 no he sido capaz de sacarlo
for i in range(1, 6, 2):
    print(i*'*')

#1.4 no he sido capaz de sacarlo solo
space = 2
for i in range(1,6,2):
    print(space*" ",i*"*")
    space = space - 1

#1.5
n = int(input('introduce un numero entero: '))
print(math.factorial(n))
rfactorial = 1
for n in range(2,rfactorial+1):
    rfactorial  = rfactorial*n
if rfactorial == math.factorial(n):
    print('El factorial es: ',rfactorial)
else:
    print('esta mal')
    
#2.Bucles iterativos con listas
'''
2.1
Write a code to find only those numbers that are divisible by 3.
Write a code to find only those numbers in the list that end with the digit 3. 
Find the minimum in the list x
Find the maximun in the list x
'''
#2.1

x = [12,43,4,1,6,343,10, 34, 12, 93, 783, 330, 896, 1, 55]
y = []
for i in x:
    if i%3 ==0:
        y.append(i)

print('Los numeros divisibles son: ', y)

j = []
for i in x:
    i = str(i)
    digit = i[-1]
    if digit == '3':
        j.append(i)
print(j)
max(x)
min(x)    
    
