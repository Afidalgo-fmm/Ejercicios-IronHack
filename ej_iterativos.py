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
# space = 2
for i in range(1,6,2):
    print(space*" ",i*"*")
    space = space - 1
