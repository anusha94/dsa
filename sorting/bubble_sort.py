'''
repeatedly swap adjacent elements if they are not in order

'''

#arr = [5,4,3,2,1]
#arr = [1,2,3,4,5]
arr = [-1,5,3,-9,0,-67]
#arr = [1,1]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j+1] < arr[j]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp


print("Sorted Array:")
print(arr)

'''
Time complexity = O(n^2) because 2 for loops
you can have a flag to determine if there were any swaps in a given pass,
if no swaps, you can terminate the loop
The above trick is useful when the array is already sorted
'''