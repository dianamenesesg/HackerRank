"""
Strings: Making Anagrams
Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?
Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.
For example, if  and , we can delete  from string  and  from string  so that both remaining strings are  and  which are anagrams.
Function Description
Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.
makeAnagram has the following parameter(s):
a: a string
b: a string
Input Format
The first line contains a single string, .
The second line contains a single string, .
Constraints
The strings  and  consist of lowercase English alphabetic letters ascii[a-z].
Output Format
Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.
Sample Input
cde
abc
Sample Output
4"""

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    for character_a in a:
        if character_a in b:
            a = a.replace(character_a,"",1)
            b = b.replace(character_a,"",1)
    num_deleted = len(a) + len(b)
    return num_deleted
#print(makeAnagram("jxwtrhvujlmrpdoqbisbwhmgpmeoke", "fcrxzwscanmligyxyvym"))

"""
Alternating Characters
A Shashank le gustan las cadenas donde los caracteres consecutivos son diferentes. Por ejemplo, le gusta , mientras que  no le gusta. Dada una cadena que solamente contiene caracteres  y , él quiere cambiarla a una cadena que le guste. Para hacerlo, solo se le permite borrar los caracteres en la cadena.
Tu tarea es encontrar la mínima cantidad requerida de borrados.
Formato de Entrada La primera linea contiene un enter  que quiere decir el número de casos de prueba. Luego siguen  lineas , con una cadena en cada linea.
Formato de Salida Imprimie la mínima cantidad requerida de pasos en cada caso de prueba.
Restricciones 
Ejemplo de Entrada
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB
Ejemplo de Salida 00
3
4
0
0
4
"""
def alternatingCharacters(s):
    #return len([1 for x in range(len(s)-1) if s[x]==s[x+1]])
    case = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            case += 1
    return case
#alternatingCharacters('AAABBBAABB')

