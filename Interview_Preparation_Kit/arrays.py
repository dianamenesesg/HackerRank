"""
 Given a  2D Array, :

 1 1 1 0 0 0
 0 1 0 0 0 0
 1 1 1 0 0 0
 0 0 0 0 0 0
 0 0 0 0 0 0
 0 0 0 0 0 0
 We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

 a b c
  d
 e f g
 There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

 For example, given the 2D array:

 -9 -9 -9  1 1 1
 0 -9  0  4 3 2
 -9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
 We calculate the following  hourglass values:

-63, -34, -9, 12,
-10, 0, 28, 23,
-27, -11, -2, 10,
9, 17, 25, 18
 Our highest hourglass value is  from the hourglass:

 0 4 3
  1
 8 6 6
 Function Description

 Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.

 hourglassSum has the following parameter(s):

 arr: an array of integers
 Input Format

 Each of the  lines of inputs  contains  space-separated integers .

 Sample Input

 1 1 1 0 0 0
 0 1 0 0 0 0
 1 1 1 0 0 0
 0 0 2 4 4 0
 0 0 0 2 0 0
 0 0 1 2 4 0
 Sample Output

 19
 Explanation

 2 4 4
  2
 1 2 4
"""

def hourglassSum(arr):
    #arr = list(map(lambda x: int(x), arr.split()))
    #arr = np.array(arr).reshape(6,6)
    mask = list([[1, 1, 1], [0, 1, 0], [1, 1, 1]])
    hourglassSum = -64
    for k in range(4):
        for i in range(4):
            NewhourglassSum = 0
            for j in range(3):
                each_new_line = arr[j+k][i:i+3]
                NewhourglassSum += sum(list(map(lambda x,
                                                y: x*y, each_new_line, mask[j])))
            if hourglassSum <= NewhourglassSum:  # np.sum(sa):
                hourglassSum = NewhourglassSum  # np.sum(sa)
    return hourglassSum


#print(hourglassSum([[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
#                    [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]))


"""
Left Rotation
A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  
left rotations are performed on array , then the array would become .
Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be 
printed as a single line of space-separated integers.
Function Description
Complete the function rotLeft in the editor below. It should return the resulting array of integers.
rotLeft has the following parameter(s):
An array of integers .
An integer , the number of rotations.
Input Format
The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
The second line contains  space-separated integers .
Constraints
Output Format
Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.
Sample Input
5 4
1 2 3 4 5
Sample Output
5 1 2 3 4
"""
def rotLeft(a, d):
    final_array = ""
    for times in range(d):
        a.append(a[0])
        a.pop(0)
    return a

#print(rotLeft([41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51], 10))

"""
Minimum Swaps 2
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
For example, given the array  we perform the following steps:
i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took  swaps to sort the array.
Function Description
Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.
minimumSwaps has the following parameter(s):
arr: an unordered array of integers
Input Format
The first line contains an integer, , the size of .
The second line contains  space-separated integers .
Constraints
Output Format
Return the minimum number of swaps to sort the given array.
Sample Input 0
4
4 3 1 2
Sample Output 0
3
"""
import math
import os
import random
import re
import sys
"""
def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    for pos, val in enumerate(arr):
        print('val', val, 'pos', pos)
        temp[val] = pos
        pos += 1
    print('temp',temp)        
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
    return swaps

print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))
"""


