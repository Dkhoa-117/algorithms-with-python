# Divine and Conquer Algorithm
# Divine array into sub-arrays by selecting a pivot
# elements that less than the pivot are kept on the left
# Continues to divine subarrays until there's only 1 element left, now the array is sorted
def partition(array, begin, end):
    pivot = array[end]
    i = begin - 1
    for j in range(begin, end):
        if pivot >= array[j]:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[end]) = (array[end], array[i + 1])

    return i + 1


def Quick_Sort(array, begin, end):
    if begin < end:
        pivotPos = partition(array, begin, end)
        Quick_Sort(array, begin, pivotPos - 1)
        Quick_Sort(array, pivotPos + 1, end)

# Testing
data = [9, 0, -3, 1, 3, 8, 7]
print("Quick Sort: ")
Quick_Sort(data, 0, len(data) -1)
print(data)

# Complexity
# 1. Time Complexities:
# - Worst Case Complexity [Big-O]: O(n^2)
# It occurs when the pivot element picked is either the greatest or the smallest element.
# This condition leads to the case in which the pivot element lies in an extreme end of the sorted array. One sub-array is always empty and another sub-array contains n - 1 elements. Thus, quicksort is called only on this sub-array.
# However, the quicksort algorithm has better performance for scattered pivots.
# - Best Case Complexity [Big-omega]: O(n*log n)
# It occurs when the pivot element is always the middle element or near to the middle element.
# - Average Case Complexity [Big-theta]: O(n*log n)
# It occurs when the above conditions do not occur.
# 2. Space Complexity:
# - The space complexity for quicksort is O(log n).

