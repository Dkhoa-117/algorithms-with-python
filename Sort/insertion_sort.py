# insertionSort(array)
#   mark first element as sorted
#   for each unsorted element X
#     'extract' the element X
#     for j <- lastSortedIndex down to 0
#       if current element j > X
#         move sorted element to the right by 1
#     break loop and insert X here
# end insertionSort

def Insertion_Sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1 
        array[j + 1] = key

# Testing
data = [8, -9, 0, 7, 3, 5]
print("Insertion Sort: ")
Insertion_Sort(data)
print(data)

# Complexity
# 1. Time Complexities:
# - Worst Case Complexity: O(n^2)
# Suppose, an array is in ascending order, and you want to sort it in descending order. In this case, worst case complexity occurs.

# Each element has to be compared with each of the other elements so, for every nth element, (n-1) number of comparisons are made.

# Thus, the total number of comparisons = n*(n-1) ~ n^2
# - Best Case Complexity: O(n)
# When the array is already sorted, the outer loop runs for n number of times whereas the inner loop does not run at all. So, there are only n number of comparisons. Thus, complexity is linear.
# - Average Case Complexity: O(n^2)
# It occurs when the elements of an array are in jumbled order (neither ascending nor descending).
# 2. Space Complexities:
# Space complexity is O(1) because an extra variable key is used.

