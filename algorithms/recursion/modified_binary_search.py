"""
Problem Statement - Find the smallest element (pivot element) in a sorted array after it has been rotated k times
clockwise direction.

Logic

1. Perform binary search
2. Update the search half based on whether mid is greater than the end. (instead of comparing with 
the search term like in binary search)
3. Last element left would be the smallest element since that's the last subset that satisfies the
condition of mid <= end

Pseudo Code -

search (arr, start, end)
    while start < end
        mid <- (start + end) // 2
        if arr[mid] > arr[end]:
            return search(arr, mid+1, end)
        else:
            return search(arr, start, mid)
    return start (returns the index of the pivot/smallest element which is also the number of times
                    the array was rotated)
    

Time Complexity - O(log n)
Space Complexity - O(log n)

Note - 
1. To find a particular element in a rotated sorted array, first find the pivot element using the
above procedure and then perform binary search on the two parts separately since each of those 
would be sorted individually which is a pre-requisite for performing binary search.

"""

def search_pivot (arr, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[end]:
            return search_pivot(arr, mid+1, end)
        else:
            return search_pivot(arr, start, mid)
    return start

a = [5,6,7,8,3]
x = search_pivot(a, 0, len(a)-1)
print(x)