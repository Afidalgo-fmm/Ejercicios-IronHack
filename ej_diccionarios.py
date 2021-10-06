#Ejercicios diccionarios

#1.1
'''
How many key-value pairs are in this dictionary?
What keys are present in this list?
What is the frequency of following words in the dictionary:
friends
taxi
jukebox
Is the word begin present in the dictionary?
Add the following words and their frequencies to the dictionary:
‘begin’: 1
‘start’: 2
‘over’: 1
‘body’: 17
Use the following code to convert the result from word_freq.keys() to a list: list(word_freq.keys())
Store the results of the above code in a variable called word.
What is the first word in the dictionary? What is the frequency of that word?
What is the last word in the dictionary? What is the frequency of that word?
'''
word_freq = {'love': 25,'conversation': 1,'every': 6,"we're": 1,'plate': 1,'sour': 1,'jukebox': 1,'now': 11,'taxi': 1,'fast': 1,'bag': 1,'man': 1,'push': 3,
  'baby': 14,'going': 1,'you': 16,"don't": 2,'one': 1,'mind': 2,'backseat': 1,'friends': 1,'then': 3,'know': 2}

'''print(len(word_freq))
print(word_freq.keys())
print(word_freq['friends'])
print(word_freq['jukebox'])
print(word_freq['taxi'])
if 'begin' in word_freq:
    print('esta clave existe.')
else:
    print('No existe esta clave')
'''
word_freq['begin'] = 1
word_freq['start'] = 2
word_freq['over'] = 1
word_freq['body'] = 17

word = list(word_freq.keys())
if word[0] in word_freq:
    a = word[0]
    #print(word_freq[a])

if word[26] in word_freq:
    b = word[26]
    #print(word_freq[b])

#1.2
'''
Can a dictionary have two key-value pairs with the same key?
'''
# No, en los diccionarios la clave siempre tiene que ser unica. Las claves van asociadas a un valor unico.

#1.3
'''
Can a dictionary have two key-value pairs with the same value but different keys?
'''
# Los valores puede repetirse dentro de un mismo diccionario al contrario que las claves.





