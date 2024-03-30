"""
Logic -

1. Divide the array into two halfs
2. Sort each half individually
3. Merge the sorted halfs

Pseudo Code -

sort(arr, start, end)
    mid = start + end // 2
    a = sort(arr, start, mid)
    b = sort(arr, mid+1, end)
    merge(a,b)
    
Time Complexity - O(nlogn)
Space Complexity - O(n)

Referrence -
 
1. https://www.youtube.com/watch?v=cVZMah9kEjI
2. https://www.geeksforgeeks.org/time-and-space-complexity-analysis-of-merge-sort/]

"""

def sort(arr):
    if len(arr) == 1:
        print(arr)
        return arr
    else:
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
    
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
        print(arr)
        return arr
                

arr = [4,3,6,4,8,0,5,9]    
print(sort(arr))