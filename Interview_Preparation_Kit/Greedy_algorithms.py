"""
Minimum Absolute Difference in an Array
Consider an array of integers, . We define the absolute difference between two elements,  and  (where ), to be the absolute value of .
Given an array of integers, find and print the minimum absolute difference between any two elements in the array. For example, given the array  we can create  pairs of numbers:  and . The absolute differences for these pairs are ,  and . The minimum absolute difference is .
Function Description
Complete the minimumAbsoluteDifference function in the editor below. It should return an integer that represents the minimum absolute difference between any pair of elements.
minimumAbsoluteDifference has the following parameter(s):
n: an integer that represents the length of arr
arr: an array of integers
Input Format
The first line contains a single integer , the size of .
The second line contains  space-separated integers .
Constraints
Output Format
Print the minimum absolute difference between any two elements in the array.
Sample Input 0
3
3 -7 0
Sample Output 0
3
"""
import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(n, arr):
    arr = sorted(arr)
    dif = math.fabs(arr[0] - arr[1])
    for i in range(n-1):
        this_dif = math.fabs(arr[i] - arr[i+1])
        if this_dif <= dif:
            dif = this_dif
    return int(dif)
print(minimumAbsoluteDifference(10, [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
