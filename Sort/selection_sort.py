# selectionSort(array, size)
#   repeat (size - 1) times
#   set the first unsorted element as the minimum
#   for each of the unsorted elements
#     if element < currentMinimum
#       set element as new minimum
#   swap minimum with first unsorted position
# end selectionSort

def Selection_Sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp

# Testing
data = [9, 0, 10, 4, 3, 2]
print("Selection sort: ")
Selection_Sort(data)
print(data)

# Complexity
# 1. Time Complexities:
# - Worst Case Complexity: O(n2)
# If we want to sort in ascending order and the array is in descending order then, the worst case occurs.
# - Best Case Complexity: O(n2)
# It occurs when the array is already sorted
# - Average Case Complexity: O(n2)
# It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

# The time complexity of the selection sort is the same in all cases. At every step, you have to find the minimum element and put it in the right place. The minimum element is not known until the end of the array is not reached.

# 2. Space Complexity:
# Space complexity is O(1) because an extra variable temp is used.

