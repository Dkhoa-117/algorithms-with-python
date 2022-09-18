def Linear_Search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

data = [5, 6, 8, 3, 12, 7, -3]

print("Linear Search: ")
print(Linear_Search(data, 7))

# Complexity
# 1. Time Complexity:
# - O(n)
# 2. Space Complexity:
# - O(1)