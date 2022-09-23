
"""
Maximum difference across the list
"""

def maxDiff(arr):
    arr_size = len(arr)
    max_diff = arr[1] - arr[0]
    min_element = arr[0]
    
    first = 0
    second = 1
     
    for i in range(1, arr_size):
        if (arr[i] - min_element > max_diff):
            max_diff = arr[i] - min_element
            second = i
            
        if (arr[i] < min_element):
            min_element = arr[i]
            first = i
    
    print('\nMaximum difference is', max_diff)
    print('First index is at', first)
    print('Second index is at', second)
    return None
     
# Driver program to test above function
maxDiff([10, 2, 6, 80, 100, 5, 500, 16])
maxDiff([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
maxDiff([-2, -1000, -5])
