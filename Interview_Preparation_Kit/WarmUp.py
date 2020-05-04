# John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
# Function Description
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.
# sockMerchant has the following parameter(s):
# n: the number of socks in the pile
# ar: the colors of each sock
# Input Format
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers describing the colors  of the socks in the pile.
# Output Format
# Return the total number of matching pairs of socks that John can sell.
# Sample Input
# 9
# 10 20 20 10 10 30 50 10 20
# Sample Output
# 3

#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    #number_socks = n
    color_each_sock = list(map(lambda x: int(x), ar.split()))
    unique_colors = set(color_each_sock)
    pairs = list(map(lambda x: math.floor(
        color_each_sock.count(x)/2), unique_colors))

    return sum(pairs)


print(sockMerchant(7, "1 2 1 2 1 3 2"))


# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.
# Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
# For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is .
# Function Description
# Complete the checkMagazine function in the editor below. It must print  if the note can be formed using the magazine, or .
# checkMagazine has the following parameters:
# magazine: an array of strings, each a word in the magazine
# note: an array of strings, each a word in the ransom note
# Input Format
# The first line contains two space-separated integers,  and , the numbers of words in the  and the ..
# The second line contains  space-separated strings, each .
# The third line contains  space-separated strings, each .
# Output Format
# Print Yes if he can use the magazine to create an untraceable replica of his ransom note. Otherwise, print No.
# Sample Input 0
# 6 4
# give me one grand today night
# give one grand today
# Sample Output 0
# Yes
# Sample Input 1
# 6 5
# two times three is not four
# two times two is four
# Sample Output 1
# No

def checkMagazine(magazine, note):
    magazine = list(map(lambda x: str(x), magazine.split()))
    note = list(map(lambda x: str(x), note.split()))
    i = -1
    for index, string in enumerate(note):
        if string in magazine:
            i += 1
            magazine.remove(string)
    print(i, index)
    if index == i:
        return 'Yes'
    else:
        return 'No'


print(checkMagazine("carefully check check hope in properly sentence the this words you",
                    "check check properly this words"))

# Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly n steps. For every step he took, he noted if it was an uphill, U, or a downhill, D step. Gary's hikes start and end at sea level and each step up or down represents a 1 unit change in altitude. We define the following terms:
# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
# For example, if Gary's path is , he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.
# Function Description
# Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.
# countingValleys has the following parameter(s):
# n: the number of steps Gary takes
# s: a string describing his path
# Input Format
# The first line contains an integer , the number of steps in Gary's hike.
# The second line contains a single string , of  characters that describe his path.
# Output Format
# Print a single integer that denotes the number of valleys Gary walked through during his hike.
# Sample Input
# 8
# UDDDUDUU
# Sample Output
# 1
# Explanation
# If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:
#
# _/\      _
#   \    /
#    \/\/
# He enters and leaves one valley.

import math
import random

def countingValleys(s):
    sea = 0
    valley = 0
    for i in s:
        if i == "U":
            i = 1
        else:
            i = -1
        if sea + i <= 0:
            sea = sea + i
            if sea == 0 and i == 1:
                valley += 1
        else:
            sea = sea + i

    return valley #numbers_of_valleys

print('countingValleys', countingValleys('DDUUUUDD'))

""" 
Jumping on the Clouds
Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. 
She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. 
Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.
For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on 
each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . 
The first path takes  jumps while the second takes .
Function Description
Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.
jumpingOnClouds has the following parameter(s):
c: an array of binary integers
Input Format
The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .
Constraints
Output Format
Print the minimum number of jumps needed to win the game.
Sample Input 0
7
0 0 1 0 0 1 0
Sample Output 0
4
"""

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    clouds = list(map(lambda x: int(x), c.split()))
    jumps = 0
    i = 0
    j = 3
    while j <= len(clouds)+1:
        jump_attempt = clouds[i:j]
        if jump_attempt[-1] == 0:
            jumps += 1
            i = j-1
            j = i+3
        else:
            jumps += 1
            i = j-2
            j = i+3
    return jumps

print(jumpingOnClouds("0 0 0 0 1 0"))

"""
Repeated String
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.
Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.
For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.
Function Description
Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.
repeatedString has the following parameter(s):
s: a string to repeat
n: the number of characters to consider
Input Format
The first line contains a single string, .
The second line contains an integer, .
Constraints
For  of the test cases, .
Output Format
Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.
Sample Input 0
aba
10
Sample Output 0
7
"""

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    magic_number = math.floor(n/len(s))
    residual = n%len(s)
    ocurrences = s.count('a')*magic_number + s[:residual].count("a")
    return ocurrences

print('ocurrences', repeatedString('aba', 12))