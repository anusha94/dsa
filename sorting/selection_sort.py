'''
given array is divided into two parts
1. subarray which is already sorted
2. remaining subarray which is unsorted

iteratively find the minimum element from the unsorted suarray
and add it to the sorted subarray

'''

#arr = [64, 25, 12, 22, 11]
#arr = []
arr = [-1,5,3,-9,0,-67]

for i in range(len(arr)):
    min_val = arr[i]
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < min_val:
            min_val = arr[j]
            min_index = j

    temp = arr[i]
    arr[i] = min_val
    arr[min_index] = temp

print("Sorted array:") 
print(arr)


'''
time complexity: O(n^2) because 2 loops
in-place because no extra space - modifies the given array itself
'''