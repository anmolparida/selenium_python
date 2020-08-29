# https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/
"""
Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1

"""

def maximumIndex(inputList):
    maxDiff = -1
    indexes = ""
    for i in range(len(inputList)):
        for j in range(i+1,len(inputList)):
            if inputList[j] > inputList[i]:
                maxDiff = max(maxDiff, j-i)
                indexes = str(i )+" and "+ str(j)
    if maxDiff == -1:
        print('no indexes found for the criteria')
    else:
        print("indexes :", indexes, ", maxDiff :" , maxDiff)


maximumIndex([34, 8, 10, 3, 2, 80, 30, 33, 1])
maximumIndex([9, 2, 3, 4, 5, 6, 7, 8, 18, 0])
maximumIndex([1, 2, 3, 4, 5, 6])
maximumIndex([6, 5, 4, 3, 2, 1])


