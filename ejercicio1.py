#Exercise 1. 
x1 = 1.1
x2 = "Ironhack"
x3 = "1.1"
x4 = True
x5 = "True"
x6 = -1

'''1.2 ->What is the difference between variables x1 and x3? '''
# x1 es una variable tipo int mientras que x3 es una variable tipo string

''' 1.3 What is the difference between variables x4 and x5?'''
# x4 es un boolean lo que significa que solo toma el valor True o False mientras que x5 es una string.

#Exercise 2
x1 = input("Please enter an integer number: ")
x2 = input("Please enter another integer number: ")
x1 = int(x1) 
x2 = int(x2) 
'''Question 1: Print the values of the two variables?'''
print(x1,x2)
'''Question 2: What is the data type of x1 and x2? Now perform simple comparisons between x1 and x2:
1. Check if the two variables are equal?

2. Check if x1 is greater than x2?

3. Check if x2 is greater than x1?

3. Check if x1 is not equal to x2?

4. Store the difference between the two variables x1 and x2 in another variable x3 (subtract the smaller number from the larger number).

5. Increment the smaller of the two variables (x1 and x2) with the difference.Use the shorthand addition operator for the same. Again check if x1 and x2 are equal or not?
'''
#1
if x1 == x2:
    print('ambas variables son iguales ')
else:
    print('son variables distintas ')

#2
if x1 > x2: #responde a la segunda pregunta
    print('x1 es mas grande que x2.')
else: # responde a la tercera pregunta
    print('x2 es mas grande que x1.')

#4 
x3 = x1 - x2
x3 = abs(x3)
txt= 'el valor de x3 es {}'
print(txt.format(x3))
