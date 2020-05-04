"""
Solve Me First
Complete the function solveMeFirst to compute the sum of two integers.
Function prototype:
int solveMeFirst(int a, int b);
where,
a is the first integer input.
b is the second integer input
Return values
sum of the above two integers
"""

def solveMeFirst(a,b):
    return a + b 

#num1 = int(input())
#num2 = int(input())
#res = solveMeFirst(num1,num2)
#print(res)

"""
Simple Array Sum
Given an array of integers, find the sum of its elements.
For example, if the array , , so return .
Function Description
Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.
simpleArraySum has the following parameter(s):
ar: an array of integers
Input Format
The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.
Output Format
Print the sum of the array's elements as a single integer.
Sample Input
6
1 2 3 4 10 11
Sample Output
31
"""
import os
import sys

def simpleArraySum(ar):
   return sum(ar)


"""
Compare the Triplets
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  
to  for three categories: problem clarity, originality, and difficulty.
We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .
Your task is to find their comparison points by comparing  with ,  with , and  with .
If , then Alice is awarded  point.
If , then Bob is awarded  point.
If , then neither person receives a point.
Comparison points is the total points a person earned.
Given  and , determine their respective comparison points.
For example,  and . For elements , Bob is awarded a point because . For the equal elements  and , no points are earned. Finally, for elements ,  so Alice receives a point. Your return array would be  with Alice's score first and Bob's second.
Function Description
Complete the function compareTriplets in the editor below. It must return an array of two integers, the first being Alice's score and the second being Bob's.
compareTriplets has the following parameter(s):
a: an array of integers representing Alice's challenge rating
b: an array of integers representing Bob's challenge rating
Input Format
The first line contains  space-separated integers, , , and , describing the respective values in triplet .
The second line contains  space-separated integers, , , and , describing the respective values in triplet .
Constraints
Output Format
Return an array of two integers denoting the respective comparison points earned by Alice and Bob.
Sample Input 0
5 6 7
3 6 10
Sample Output 0
1 1
"""
def compareTriplets(a, b):
    alice = 0
    bob = 0
    for categories in range(3):
        if a[categories] > b[categories]:
            alice += 1
        elif a[categories] < b[categories]:
            bob +=1
    return [alice, bob]

#print(compareTriplets([5,9,7], [3, 6, 6]))

"""
A Very Big Sum
Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.
Function Description
Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
aVeryBigSum has the following parameter(s):
ar: an array of integers .
Input Format
The first line of the input consists of an integer .
The next line contains  space-separated integers contained in the array.
Output Format
Print the integer sum of the elements in the array.
Constraints
Sample Input
5
1000000001 1000000002 1000000003 1000000004 1000000005
Output
5000000015
Note:
The range of the 32-bit integer is .
When we add several integer values, the resulting sum might exceed the above range. You might need to use long long int in 
C/C++ or long data type in Java to store such sums.
"""
import math
import os
import random
import re
import sys

def aVeryBigSum(ar_count, ar):
    evens = 0
    odds = 0
    for index, element in enumerate(ar):
        if index%2 == 0:
            evens += element
        else:
            odds += element
    total_sum = evens + odds

    return total_sum

#print(aVeryBigSum(5, [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))

"""
Diagonal Difference
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below:
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .
Function description
Complete the  function in the editor below. It must return an integer representing the absolute diagonal difference.
diagonalDifference takes the following parameter:
arr: an array of integers .
Input Format
The first line contains a single integer, , the number of rows and columns in the matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .
Constraints
Output Format
Print the absolute difference between the sums of the matrix's two diagonals as a single integer.
Sample Input
3
11 2 4
4 5 6
10 8 -12
Sample Output
15
"""

def diagonalDifference(n, arr):
    left_to_right = []
    right_to_left = []
    for i in range(n):
        for j in range(n):
            if i ==j:
                left_to_right.append(arr[i][j])
            if i + j == n-1:
                right_to_left.append(arr[i][j])
    diff = math.fabs(sum(left_to_right) - sum(right_to_left))
    return int(diff)

#print(diagonalDifference(3, [[11, 2, 4], [4, 5, 6], [10, 8 , -12]]))

"""
Plus Minus
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
For example, given the array  there are  elements, two positive, two negative and one zero. Their ratios would be ,  and . It should be printed as
0.400000
0.400000
0.200000
Function Description
Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.
plusMinus has the following parameter(s):
arr: an array of integers
Input Format
The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .
Constraints
Output Format
You must print the following  lines:
A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
"""

import math
import os
import random
import re
import sys

def plusMinus(n, arr):
    positive = round(len(list(filter(lambda x: x>0, arr)))/n, 6)
    negative = round(len(list(filter(lambda x: x<0, arr)))/n, 6)
    zero = round(len(list(filter(lambda x: x==0, arr)))/n, 6)
#    print('{:.6f}'.format(positive))
#    print('{:.6f}'.format(negative))
#    print('{:.6f}'.format(zero))
    print('{:.6f}'.format(positive), '{:.6f}'.format(negative), '{:.6f}'.format(zero), sep='\n')

#plusMinus(6, [-4, 3, -9, 0, 4, 1])

"""
Staircase
Consider a staircase of size :
   #
  ##
 ###
####
Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
Write a program that prints a staircase of size .
Function Description
Complete the staircase function in the editor below. It should print a staircase as described above.
staircase has the following parameter(s):
n: an integer
Input Format
A single integer, , denoting the size of the staircase.
Constraints
Output Format
Print a staircase of size  using # symbols and spaces.
Note: The last line must have  spaces in it.
Sample Input
6 
Sample Output

     #
    ##
   ###
  ####
 #####
######
"""

def staircase(n):
	for i in range(1,n+1):
		print(' '*(n-i)+'#'*i)
		
#staircase(6)


"""
Mini-Max Sum
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
For example, . Our minimum sum is  and our maximum sum is . We would print
16 24
Function Description
Complete the miniMaxSum function in the editor below. It should print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.
miniMaxSum has the following parameter(s):
arr: an array of  integers
Input Format
A single line of five space-separated integers.
Constraints
Output Format
Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)
Sample Input
1 2 3 4 5
Sample Output
10 14
"""

def miniMaxSum(arr):
	new_arr = []
	for i in range(0,5):
		arr_complet = arr[:]
		arr_complet.pop(i)
		new_arr.append(sum(arr_complet)) 
	#return min(new_arr), max(new_arr)
	print(min(new_arr), max(new_arr))
		
miniMaxSum([1,2,3,4,5])

"""
Birthday Cake Candles
You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.
For example, if your niece is turning  years old, and the cake will have  candles of height , , , , she will be able to blow out  candles successfully, since the tallest candles are of height  and there are  such candles.
Function Description
Complete the function birthdayCakeCandles in the editor below. It must return an integer representing the number of candles she can blow out.
birthdayCakeCandles has the following parameter(s):
ar: an array of integers representing candle heights
Input Format
The first line contains a single integer, , denoting the number of candles on the cake.
The second line contains  space-separated integers, where each integer  describes the height of candle .
Constraints
Output Format
Return the number of candles that can be blown out on a new line.
Sample Input 0
4
3 2 1 3
Sample Output 0
2
"""
import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    tallest = max(ar)
    bl_out = ar.count(tallest)
    return bl_out
print(birthdayCakeCandles([4,4,3,2,10]))


"""
Time Conversion
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
Function Description
Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
TimeConversion has the following parameter(s):
s: a string representing time in  hour format
Input Format
A single string  containing a time in -hour clock format (i.e.:  or ), where  and .
Constraints
All input times are valid
Output Format
Convert and print the given time in -hour format, where .
Sample Input 0
07:05:45PM
Sample Output 0
19:05:45
"""

import os
import sys

def timeConversion(s):
    hh, mm, ss = s[:-2].split(':')
    is_P = bool(s[-2:] == 'PM')
    hh = int(hh) % 12 + is_P * 12
    
    return "".join([str(hh).zfill(2),':',str(mm), ':', str(ss)])
    #print(('%02d:%02d:%02d') % (int(hh), int(mm), int(ss)))
print(timeConversion('07:05:45PM'))

"""
Grading Students
HackerLand University has the following grading policy:
Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:
If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
For example,  will be rounded to  but  will not be rounded because the rounding would result in a number that is less than .
Given the initial value of  for each of Sam's  students, write code to automate the rounding process.
Function Description
Complete the function gradingStudents in the editor below. It should return an integer array consisting of rounded grades.
gradingStudents has the following parameter(s):
grades: an array of integers representing grades before rounding
Input Format
The first line contains a single integer, , the number of students.
Each line  of the  subsequent lines contains a single integer, , denoting student 's grade.
Constraints
Output Format
For each , print the rounded grade on a new line.
Sample Input 0
4
73
67
38
33
Sample Output 0
75
67
40
33
Explanation 0
image
Student  received a , and the next multiple of  from  is . Since , the student's grade is rounded to .
Student  received a , and the next multiple of  from  is . Since , the grade will not be modified and the student's final grade is .
Student  received a , and the next multiple of  from  is . Since , the student's grade will be rounded to .
Student  received a grade below , so the grade will not be modified and the student's final grade is .
"""
def gradingStudents(grades_list):
    final_list = []
    for grade in grades_list:
        if grade < 38:
            final_list.append(grade)

        else:
            grade_old = grade
            while  not grade%5==0:
                grade += 1
            if grade - grade_old < 3:
                final_list.append(grade)
            else:
                final_list.append(grade_old)
                
    return final_list  

#print(gradingStudents([74, 67, 38, 33]))

"""
Apple and Orange
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where  is the start point, and  is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .
Apple and orange(2).png
When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. A negative value of  means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right.
Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?
For example, Sam's house is between  and . The apple tree is located at  and the orange at . There are  apples and  oranges. Apples are thrown  units distance from , and  units distance. Adding each apple distance to the position of the tree, they land at . Oranges land at . One apple and two oranges land in the inclusive range  so we print
1
2
Function Description
Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.
countApplesAndOranges has the following parameter(s):
s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.
"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    list_A = [1 for apple in apples if (s <= a + apple) and (a + apple <= t)]
    list_B = [1 for orange in oranges if (s <= b + orange) and (b + orange <= t)]
    
    return "{0} {1}".format(len(list_A), len(list_B))

print(countApplesAndOranges(7, 10, 4, 12, [2, 3, -4 ], [3, -2, -4]))    

"""
Kangaroo
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
The first kangaroo starts at location  and moves at a rate of  meters per jump.
The second kangaroo starts at location  and moves at a rate of  meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.
For example, kangaroo  starts at  with a jump distance  and kangaroo  starts at  with a jump distance of . After one jump, they are both at , (, ), so our answer is YES.
Function Description
Complete the function kangaroo in the editor below. It should return YES if they reach the same position at the same time, or NO if they don't.
kangaroo has the following parameter(s):
x1, v1: integers, starting position and jump distance for kangaroo 1
x2, v2: integers, starting position and jump distance for kangaroo 2
Input Format
A single line of four space-separated integers denoting the respective values of , , , and .
Constraints
Output Format
Print YES if they can land on the same location at the same time; otherwise, print NO.
Note: The two kangaroos must land at the same location after making the same number of jumps.
Sample Input 0
0 3 4 2
Sample Output 0
YES
"""

def kangaroo(x1, v1, x2, v2):
    show_time = 'NO'
    for i in range(10_000):
        if x1 + v1*i == x2 + v2*i:
            show_time = 'YES'
            break
    if show_time == "NO":
        return "NO"
    else:
        return show_time

#print(kangaroo(0,2,5,3)) 

"""
Between Two Sets
You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:
The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.
For example, given the arrays  and , there are two numbers between them:  and . , ,  and  for the first value. Similarly, ,  and , .
Function Description
Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.
getTotalX has the following parameter(s):
a: an array of integers
b: an array of integers
Input Format
The first line contains two space-separated integers,  and , the number of elements in array  and the number of elements in array .
The second line contains  distinct space-separated integers describing  where .
The third line contains  distinct space-separated integers describing  where .
Constraints
Output Format
Print the number of integers that are considered to be between  and .
Sample Input
2 3
2 4
16 32 96
Sample Output
3
"""
def getTotalX(a, b):
    min_value = min(a)
    max_value = max(b)
    total = [1 if (sum(list(map(lambda x: number%x, a)))+sum(list(map(lambda y: y%number, b))))==0 else 0 
    for number in range(min_value, max_value + 1) ]
    return sum(total)

print( getTotalX([2], [20, 30, 12]))

"""
Breaking the Records
Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.
For example, assume her scores for the season are represented in the array . Scores are in the same order as the games played. She would tabulate her results as follows:
                                 Count
Game  Score  Minimum  Maximum   Min Max
 0      12     12       12       0   0
 1      24     12       24       0   1
 2      10     10       24       1   1
 3      24     10       24       1   1
Given Maria's scores for a season, find and print the number of times she breaks her records for most and least points scored during the season.
Function Description
Complete the breakingRecords function in the editor below. It must return an integer array containing the numbers of times she broke her records. Index  is for breaking most points records, and index  is for breaking least points records.
breakingRecords has the following parameter(s):
scores: an array of integers
Input Format
The first line contains an integer , the number of games.
The second line contains  space-separated integers describing the respective values of .
Constraints
Output Format
Print two space-seperated integers describing the respective numbers of times her best (highest) score increased and her worst (lowest) score decreased.
Sample Input 0
9
10 5 20 20 4 5 2 25 1
Sample Output 0
2 4
"""
def breakingRecords(scores):
    worst, best = [], []
    min_record = scores[0]
    for score in scores[1:]:
        if score > max(best+[min_record]) :
            best.append(score)
        elif score < min(worst+[min_record], default=0) :
            worst.append(score)

    return len(best), len(worst)
crazy_test = '99964 99958 99917 99867 99432 99310 99288 98977 98861 98667 98637 98590 98518 98506 98278 98248 98154 98093 98065 98011 97576 97510 97148 97094 97055 96828 96826 96610 96507 96474 96092 95777 95774 95723 95654 95606 95512 95487 95476 95366 95212 95126 94856 94738 94516 94322 94184 94177 94132 93680 93674 93480 93413 93380 93217 93198 93158 93027 92858 92856 92524 92522 92436 92287 92189 92126 92005 91943 91605 91534 91321 91154 90921 90751 90670 90618 90502 90351 90248 90059 90022 89927 89445 89153 88939 88928 88877 88802 88787 88780 88776 88750 88357 88330 88288 88270 88204 88188 88135 88112 88072 87839 87798 87761 87699 87616 87616 87581 87355 87339 87174 87077 86990 86890 86831 86656 86318 86315 86200 86192 86122 86104 85956 85659 85587 85543 85385 85381 85308 85100 85074 85051 84842 84819 84744 84652 84502 84419 84343 84170 84064 84051 84018 84007 83628 83445 82810 82656 82514 82497 82449 82406 82336 82181 82152 81674 81568 81531 81520 81511 81422 81364 81253 81215 81151 81145 81058 81032 81024 80915 80913 80839 80664 80631 80485 80330 80218 80145 80055 80012 79999 79803 79658 79629 79529 79411 79168 78573 78568 78566 78371 78081 78069 78001 77826 77556 77503 77396 77382 77376 77312 77237 77163 77002 76799 76739 76671 76557 76533 76512 76379 76375 76323 76236 76231 76068 75929 75723 75583 75371 75259 75143 75024 74988 74751 74740 74737 74397 74380 74324 74303 74277 74238 74126 74036 73741 73720 73676 73560 73374 73330 73275 72881 72848 72816 72800 72665 72638 72452 72420 72266 72241 71987 71851 71647 71558 71262 71107 70965 70933 70761 70752 69986 69936 69639 69595 69592 69287 69272 69194 68968 68963 68882 68787 68761 68692 68637 68523 68442 68417 68415 68194 68108 68079 68063 68049 67971 67815 67715 67634 67611 67542 67462 67450 67370 67339 67253 67127 67107 66700 66563 66449 66389 66375 66369 66355 66343 66232 66144 66142 65955 65511 65365 65361 65314 65234 65096 65055 65036 64803 64539 64490 64248 64192 63955 63818 63813 63788 63615 63577 63574 63552 63506 63362 62779 62743 62586 62505 62378 62174 61957 61946 61931 61913 61894 61720 61676 61665 61483 61151 61012 60905 60891 60831 60815 60682 60678 60575 60569 60097 60072 59972 59742 59680 59656 59602 59380 59084 58944 58904 58868 58847 58809 58775 58735 58709 58627 58626 58568 58522 58441 58354 58343 58301 58260 58212 57913 57907 57887 57839 57765 57747 57746 57640 57552 57432 57431 57426 57394 57228 57053 56859 56846 56814 56779 56701 56386 56360 56311 56307 56271 56233 56183 56074 55860 55855 55725 55724 55714 55710 55505 55473 55466 55376 55208 55142 55037 54863 54857 54804 54747 54579 54567 54525 54511 54494 54492 54447 54284 54120 53986 53923 53920 53891 53668 53660 53556 53424 53322 53294 53161 52992 52934 52924 52869 52774 52634 52628 52405 52390 52297 52288 52126 52125 51996 51878 51861 51740 51739 51681 51655 51488 51487 51384 51305 51251 51135 50776 50739 50677 50655 50516 50473 50431 50427 50393 50342 50318 50252 49954 49694 49401 49334 49059 48890 48587 48562 48497 48478 48229 48212 48179 47935 47821 47760 47702 47605 47449 47330 47303 47170 47113 46888 46841 46767 46373 46287 46272 46209 46192 46179 46139 46065 45983 45923 45884 45727 45704 45589 45578 45522 45378 45228 45205 45205 45184 45150 45103 45061 44998 44956 44946 44478 44423 44395 44330 44316 44251 44227 44192 43991 43945 43944 43862 43835 43432 43335 43190 43062 42988 42941 42916 42863 42732 42683 42668 42637 42427 42093 42018 41928 41900 41872 41722 41685 41632 41499 41101 41011 40999 40776 40650 40516 40456 40373 40257 40141 39866 39816 39792 39678 39573 39300 39275 39263 39046 38915 38875 38868 38822 38819 38668 38635 38609 38296 38230 38212 38100 38072 37784 37727 37625 37496 37449 37382 37351 37273 37267 36979 36852 36631 36529 36528 36180 35901 35883 35831 35820 35732 35646 35597 35434 35214 35153 34806 34800 34712 34695 34667 34549 34396 34180 34148 34143 34040 33978 33865 33707 33649 33623 33546 33461 32849 32849 32704 32580 32509 32505 32456 32401 32323 32085 32064 32050 31955 31827 31821 31733 31669 31560 31540 31531 31249 31138 31035 30920 30654 30645 30531 30502 30465 30412 30403 30386 30244 30072 29992 29945 29928 29819 29741 29620 29580 29255 29214 28950 28893 28728 28674 28659 28548 28401 28206 28192 28179 28137 27914 27705 27625 27616 27554 27474 27417 27414 27223 27184 27103 27067 27030 26970 26799 26695 26616 26443 26301 26255 26106 25724 25715 25671 25508 25425 25408 25316 25243 25041 25033 24548 24522 24338 24289 24119 23847 23783 23671 23671 23621 23618 23605 23458 23386 23126 22523 22210 22140 22105 22053 22016 21925 21840 21820 21816 21632 21562 21542 21519 21406 21343 21330 21234 21057 21003 20799 20771 20482 20439 20269 20269 19979 19938 19710 19673 19536 19186 19160 19036 18900 18842 18601 18593 18573 18323 18209 17990 17921 17856 17746 17641 17534 17500 17443 17096 16652 16610 16597 16564 16410 16406 16377 16156 16063 16013 15981 15939 15667 15621 15517 15258 15257 15242 14948 14819 14796 14777 14746 14698 14625 14596 14454 14259 14253 14221 13994 13909 13907 13632 13532 13445 13207 13183 13060 13036 13024 12650 12592 12556 12555 12529 12518 12506 12418 12403 12401 12392 12383 11955 11898 11761 11591 11575 11495 11339 11318 11313 11039 10942 10847 10757 10750 10661 10654 10631 10553 10513 10491 10466 10176 10175 9931 9920 9847 9623 9550 9296 9132 9119 9053 9005 9002 8903 8899 8787 8671 8625 8625 8476 8384 7994 7939 7881 7845 7834 7716 7687 7653 7440 7432 7393 7379 7345 7277 7273 7230 7208 7180 7179 7108 7046 7036 6915 6826 6516 6500 6392 6258 6199 6089 6048 5943 5773 5667 5654 5585 5474 5407 5378 5292 5221 5220 5176 5043 4871 4785 4784 4775 4544 4500 4469 4409 4395 4354 4327 4233 4134 4127 4084 4023 3959 3916 3872 3866 3810 3732 3663 3454 3362 3323 3320 3279 3133 2994 2988 2836 2826 2641 2485 2198 2014 1893 1890 1837 1794 1784 1512 1329 1160 1035 1032 1015 934 932 723 470 384 297 238 233 154 116 106'
crazy_test = list(map(int, crazy_test.split(' ')))

#print(breakingRecords(crazy_test)) 


"""
Birthday Chocolate
Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.
Consider the chocolate bar as an array of squares, . She wants to find segments summing to Ron's birth day,  with a length equalling his birth month, . In this case, there are two segments meeting her criteria:  and .
Function Description
Complete the birthday function in the editor below. It should return an integer denoting the number of ways Lily can divide the chocolate bar.
birthday has the following parameter(s):
s: an array of integers, the numbers on each of the squares of chocolate
d: an integer, Ron's birth day
m: an integer, Ron's birth month
Input Format
The first line contains an integer , the number of squares in the chocolate bar.
The second line contains  space-separated integers , the numbers on the chocolate squares where .
The third line contains two space-separated integers,  and , Ron's birth day and his birth month.
Constraints
, where ()
Output Format
Print an integer denoting the total number of ways that Lily can portion her chocolate bar to share with Ron.
Sample Input 0
5
1 2 1 3 2
3 2
Sample Output 0
2
"""
def birthday(n, s, d, m):
    ways = 0       
    for i in range(n):
        if sum(s[i:i+m]) == d:
            ways += 1
    return ways

print(birthday(5, [1, 2, 1, 3, 2], 3, 2))

"""
Divisible Sum Pairs
You are given an array of  integers, , and a positive integer, . Find and print the number of  pairs where  and  +  is divisible by .
For example,  and . Our three pairs meeting the criteria are  and .
Function Description
Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.
divisibleSumPairs has the following parameter(s):
n: the integer length of array 
ar: an array of integers
k: the integer to divide the pair sum by
Input Format
The first line contains  space-separated integers,  and .
The second line contains  space-separated integers describing the values of .
Constraints
Output Format
Print the number of  pairs where  and  +  is evenly divisible by .
Sample Input
6 3
1 3 2 6 1 2
Sample Output
 5
"""  

def divisibleSumPairs(n, k, ar):
    lenpairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if not (ar[i] + ar[j])%k:
                lenpairs += 1
    return lenpairs                

print(divisibleSumPairs(6, 5, [1,2,3,4,5,6]))