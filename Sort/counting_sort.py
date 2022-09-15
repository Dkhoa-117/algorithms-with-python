# countingSort(array, size)
#   max <- find largest element in array
#   initialize count array with all zeros
#   for j <- 0 to size
#     find the total count of each unique element and 
#     store the count at jth index in count array
#   for i <- 1 to max
#     find the cumulative sum and store it in count array itself
#   for j <- size down to 1
#     restore the elements to array
#     decrease count of each element restored by 1

def Counting_Sort(array):
    max = array[0]
    size = len(array)
    for i in range(1, size):
        if array[i] > max:
            max = array[i]
    output = [0]*size
    count = [0]*(max + 1)
    for i in range(size):
        count[array[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    for i in range(size):
        array[i] = output[i]

data = [3, 9, 3, 7, 0, 2, 6, 8]
print("Counting Sort: ")
Counting_Sort(data)
print(data)

# Complexity
# 1. Time Complexities:
# - Worst Case Complexity: O(n+k)
# - Best Case Complexity: O(n+k)
# - Average Case Complexity: O(n+k)
# In all the above cases, the complexity is the same because no matter how the elements are placed in the array, the algorithm goes through n+k times.
# 2. Space Complexity:
# - The space complexity of Counting Sort is O(max). Larger the range of elements, larger is the space complexity.
