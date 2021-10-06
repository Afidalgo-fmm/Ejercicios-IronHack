#ejercicios de listas

#1.1
'''
How many elements are in the list?
Using indexes, find out which is the first element in the list?
Using indexes, find out which is the last element in the list?
What is the index of element 90 in the list?
Which are the first 8 elements in the list?
Append elements 100 and 110 to the list?
'''
lst = [1,2,34,5,3,12,9, 8, 67, 89, 98, 90, 39, 21, 45, 46, 23, 13]
print(len(lst))
print(lst[0])
print(lst[-1])
print(lst.index(90))
print(lst[:8])
lst.append(110)
lst.append(100)
print(lst)


#1.2
'''
Una lista puede tener el mismo elemento repetido.
'''
  #ejemplo:
lista_prueba = (1,1,1,1,1,1,1,1,1)
print(lista_prueba)