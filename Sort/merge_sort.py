# Divine and Conquer Strategy
# Divine array into sub-arrays
# When reach the base case, we conquer by soft those sub-array
# Combine those sorted subarrays to get final sorted arrays

def Merge_Sort(array):
    if len(array) > 1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        Merge_Sort(L)
        Merge_Sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

# Testing
data = [10, 4, 8, 9, -1, 6, -7, 0]
print("Merge Sort: ")
Merge_Sort(data)
print(data)

# Complexity
# 1. Time Complexities:
# Best Case Complexity: O(n*log n)

# Worst Case Complexity: O(n*log n)

# Average Case Complexity: O(n*log n)
# 2. Space Complexity:
# The space complexity of merge sort is O(n).



