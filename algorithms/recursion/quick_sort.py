"""
Logic -

1. Pick a random pivot element (usually the last one)
2. Partition the array into three subarrays respectively containing the elements smaller than 
the pivot, the pivot element itself, and the elements larger than the pivot.
3. Recursively quick-sort the first and last subarrays.

Pseudo Code-

sort(arr)
    p = partition(arr)
    sort(arr[:r])
    sort(arr[r:])

partition(arr, pivot)
    pivot = arr[-1]
    l = 0 (tracks index of the last element smaller than pivot element)
    for i <- 0 to len(arr) - 1
        if arr[i] < pivot (moving all elements lesser than pivot to the front)
            swap arr[l], arr[i]
            l <- l + 1
    swap arr[l], arr[-1]
    return l
    
Time Complexity - 

Worst Case (when pivot element lies in the extremes always) - O(n^2)
Average Case (when pivot element lies in the middle on average) - O(nlogn)

Space Complexity - O(1)

Referrence -
1. https://www.youtube.com/watch?v=9KBwdDEwal8
2. https://www.geeksforgeeks.org/time-and-space-complexity-analysis-of-quick-sort/

Note - 

1. In python, when a list is passed as a parameter, a reference to the original list is passed. 
Therefore any changes to the list within the function is reflected on the original list outisde the
function as well.
2. Be careful about the start and end of the sub-array during recursion, it does not always start
from 0. 
3. Keep in mind for loop runs till one less than the upper limit by default.
"""

def sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        sort(arr, start, p-1)
        sort(arr, p+1, end)

def partition(arr, start, end):
    pivot = arr[end]
    l = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[l], arr[i] = arr[i], arr[l]
            l += 1
    arr[l], arr[end] = arr[end], arr[l] 
    return l

A = [5, 2, 3, 1, 5, 2]
sort(A, 0, len(A)-1)
print(A)
