def Binary_Search(array, target, begin, end):
    if begin > end:
        return -1
    mid = begin + (end - begin)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return Binary_Search(array, target, mid + 1, end)
    else:
        return Binary_Search(array, target, begin, mid - 1)
data = [1, 2, 4, 5, 6, 8, 10]

print("Binary Search: ")
print(Binary_Search(data, 7, 0, len(data) - 1))

# Complexity
# 1. Time Complexities:
# - Best case complexity: O(1)
# - Average case complexity: O(log n)
# - Worst case complexity: O(log n)
# 2. Space Complexity:
# - The space complexity of the binary search is O(1).