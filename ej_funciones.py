#Ejercicio funciones
'''
Define the function generation calculator & add both parameters to represent both variables we are going to need in this function.
Determine generation as a birth year (we need to know the year to be able to calculate)
Print the results
Write conditionals for each generation. For example, if you were born before 1949 you would be a “silent generation”.
Define variables for each result
Show results
+-----------------+---------------------+
|  birth_year     |      generation     |
+-----------------+---------------------+
|     < 1949      |  silent generation  |
+-----------------+---------------------+
|     < 1969      |     baby boomer     |
+-----------------+---------------------+
|     < 1981      |     X generation    |
+-----------------+---------------------+
|     < 1994      |      millennial     |
+-----------------+---------------------+
|     > 1994      |    Z generation     |
+-----------------+---------------------+

'''
def calculadora_generacional(nombre,año_nacimiento):
    if año_nacimiento < 1949:
        return nombre + ' es de la generación silenciosa.'
    elif año_nacimiento< 1969:
        return nombre + ' es de la generación baby boomer.'
    elif año_nacimiento < 1981:
        return nombre + ' es de la generación X.'
    elif año_nacimiento < 1994:
         return nombre + ' es de la generación millennial.'
    elif año_nacimiento > 1994:
        return nombre + ' es de la generación Z.'

#ejemplos:
name1 = "Jonh"
birth_year1 = 1989
resultado1 = calculadora_generacional(name1,birth_year1)
print(resultado1)
name2 = "Mari"
birth_year2 = 1995
resultado2 = calculadora_generacional(name2,birth_year2)
print(resultado2)
name3 = "Mich"
birth_year3 = 1960
resultado3 = calculadora_generacional(name3, birth_year3)
print(resultado3)
