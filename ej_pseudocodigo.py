#Ejercicio Pseudocodigo
'''
Instrucciones:
You are witnessing an epic battle between two powerful sorcerers: Gandalf and Saruman. 
Each sorcerer has 10 spells of different powers in their mind and they are going to throw them one after the other. 
The winner of the duel will be the one who wins more of those clashes between spells. 
Spells are represented as a list of 10 integers whose value equals the power of the spell.

You will create two variables, one for each sorcerer, 
where the total of number of clashes won by each sorcerer will be stored. 
Depending on which variable is greater at the end of the duel, 
you will show one of the following three results on the screen:
'''

'''
Desarrollo:
Para poder hacer el programa tengo que definir tres variables: puntuacion de gandelf(pgandalf), puntaacion de saruman(psaruman)
y los empates(empate); con estas variables voy acumulando el numero de victorias de cada uno segun la comparacion de daño que hace cada hechizo.
Dicho daño esta definido en las listas ya dadas(cada elemento de las listas es el daño de cada hechizo).
'''
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
#creo 3 variables para determinar quien de los dos magos ha ganado mas encuentros.
pgandalf= 0
psaruman = 0
empate = 0 # en el caso de que ambos hechizos sean iguales se suma el encuentro aqui.

#Bucle iterativo for para poder comparar los elementos de cada lista

for i in range(0,len(gandalf)):
    if gandalf[i] == saruman[i]:  #El Bucle condicional nos ayuda adeterminar de quien ha sido la victoria en cada encuentro.
        empate +=1
    elif gandalf[i] > saruman[i]:
        pgandalf +=1
    else:
        psaruman +=1
#print(pgandalf)
#print(psaruman)
#Con el siguiente bucle condicional vemos quien ha sido el que mas victorias se ha llevado.
#Para saber quien ha ganado hay que poner hay que comparar el numero de victorias.

if psaruman < pgandalf:
    print('Gandalf es el vencedor!!')
elif psaruman > pgandalf:
    print('El vencedor es Saruman!!')
else:
    print('El encuentro ha terminado en Empate!!')
    print('Han habido un total de ', str(empate))