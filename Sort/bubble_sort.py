
# bubbleSort(array)
#   for i <- 1 to indexOfLastUnsortedElement-1
#     if leftElement > rightElement
#       swap leftElement and rightElement
# end bubbleSort

def Bubble_Sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
        
# Testing
data = [6, 0, -10, 8, 4, 9]
print("Bubble Sort: ")
Bubble_Sort(data)
print(data);

# Complexity
# 1. Time Complexities
# - Worst Case Complexity: O(n^2)
# If we want to sort in ascending order and the array is in descending order then the worst case occurs.
# - Best Case Complexity: O(n)
# If the array is already sorted, then there is no need for sorting.
# - Average Case Complexity: O(n^2)
# It occurs when the elements of the array are in jumbled order (neither ascending nor descending).
# 2. Space Complexity
# - Space complexity is O(1) because an extra variable is used for swapping.

