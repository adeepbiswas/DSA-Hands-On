"""
Problem Statement - Find the kth element of an unordered array

Logic -

1. Select random pivot (usually last element) and partition the array
2. If the pivot ends up in 'k-1'th place then we have found the answer
3. Else do quick select on left partition if pivot index > k-1
4. Else do quick select on right partition if pivot index < k-1

Pseudo Code - 

partition(arr, start, end, pivot)
    i = start
    l = start (keeps track of the next place where a element smaller than pivot should be placed)
    for i <- start to end-1
        if arr[i] < pivot
            swap arr[i], arr[l]
            l <- l+1
    swap arr[l], pivot
    return l

quickselect(arr, start, end, k)
    pivot <- last element of the list
    index <- partition(arr, start, end, pivot)
    if index == k-1:
        return pivot
    else if index > k-1:
        quickselect(arr, start, index, k)
    else if index < k-1:
        quickselect(arr, index, end, k)

Time Complexity:

1. In the worst case, the time complexity is O(n^2), where n is the number of elements in the array. 
This happens when the pivot is consistently chosen poorly, leading to unbalanced partitions, 
resembling the worst-case behavior of quicksort.
2. In the average case, the time complexity is O(n), where n is the number of elements in the array. 
This assumes a good pivot selection strategy, resulting in balanced partitions.
3. In the best case, the time complexity is O(n), achieved when the pivot selection consistently 
divides the array into approximately equal-sized partitions.

Space Complexity:

The space complexity of the provided algorithm is O(log n) in the average and best cases. 
This is because the algorithm uses recursion, and the maximum depth of the recursion tree is 
logarithmic with respect to the number of elements in the array.
However, in the worst case, the space complexity can degrade to O(n), as the recursion depth may 
reach the maximum number of elements in the array.

Note -
1. Quickselect takes O(n) which is better than O(nlogn) from sorting the array first and then
picking the kth element.
2. Make sure to return all recursive calls. Without returning the result, the function won't 
propagate the selected element up the call stack.
"""

def partition(arr, start, end, pivot):
    l = start
    for i in range(start,end-1):
        if arr[i] < pivot:
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
    arr[l], arr[end - 1] = arr[end - 1], arr[l] 
    return l

def quickselect(arr, start, end, k):
    pivot = arr[end-1]
    index = partition(arr, start, end, pivot)
    if index == k-1:
        return pivot
    elif index > k-1:
        return quickselect(arr, start, index, k)
    elif index < k-1:
        return quickselect(arr, index+1, end, k)
        
        
a  = [4,6,3,7,2,9]
x = quickselect(a, 0, len(a), 3)
print(x)