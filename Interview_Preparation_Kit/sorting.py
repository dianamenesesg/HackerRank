"""
Sorting: Bubble Sort
Consider the following version of Bubble Sort:
for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
    
}
Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:
Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
First Element: firstElement, where  is the first element in the sorted array.
Last Element: lastElement, where  is the last element in the sorted array.
Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.
For example, given a worst-case but small array to sort:  we go through the following steps:
swap    a       
0       [6,4,1]
1       [4,6,1]
2       [4,1,6]
3       [1,4,6]
It took  swaps to sort the array. Output would be
Array is sorted in 3 swaps.  
First Element: 1  
Last Element: 6  
Function Description
Complete the function countSwaps in the editor below. It should print the three lines required, then return.
countSwaps has the following parameter(s):
a: an array of integers .
Input Format
The first line contains an integer, , the size of the array .
The second line contains  space-separated integers .
Constraints
Output Format
You must print the following three lines of output:
Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
First Element: firstElement, where  is the first element in the sorted array.
Last Element: lastElement, where  is the last element in the sorted array.
Sample Input 0
3
1 2 3
Sample Output 0
Array is sorted in 0 swaps.
First Element: 1
Last Element: 3
"""
def swaping(n, a):
    swaps = 0 
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps = swaps + 1
    print('Array is sorted in', swaps, 'swaps.')
    print('First Element:', a[0])
    print('Last Element:', a[-1])
#    return swaps
#swaping(3, [1, 2, 3])

"""
Mark and Toys
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.
Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if  and Mark has  to spend, he can buy items  for , or  for  units of currency. He would choose the first group of  items.
Function Description
Complete the function maximumToys in the editor below. It should return an integer representing the maximum number of toys Mark can purchase.
maximumToys has the following parameter(s):
prices: an array of integers representing toy prices
k: an integer, Mark's budget
Input Format
The first line contains two integers,  and , the number of priced toys and the amount Mark has to spend.
The next line contains  space-separated integers 
Constraints
A toy can't be bought multiple times.
Output Format
An integer that denotes the maximum number of toys Mark can buy for his son.
Sample Input
7 50
1 12 5 111 200 1000 10
Sample Output
4
"""
def maximumToys(prices, k, n):
    prices = sorted(prices)
    for i in range(n):
        if sum(prices[:i]) <= k:
            toys = len(prices[:i])
        else:
            break
        
    return toys
print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50, 7))


