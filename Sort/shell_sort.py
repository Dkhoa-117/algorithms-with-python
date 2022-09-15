# shellSort(array, size)
#   for interval i <- size/2n down to 1
#     for each interval "i" in array
#         sort all the elements at interval "i"
# end shellSort

def Shell_Sort(array, size):
    interval = size//2
    while interval > 0:
        for i in range(interval, size):
            temp = array[i]

            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j-=interval
            array[j] = temp
        interval //= 2


data = [9, 8, 3, 7, 5, 6, 4, 1]
size = len(data)
Shell_Sort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

# Complexity
# 1. Time Complexities:
# - Worst Case Complexity: less than or equal to O(n^2)
# Worst case complexity for shell sort is always less than or equal to O(n^2).

# According to Poonen Theorem, worst case complexity for shell sort is Θ(Nlog N)2/(log log N)2) or Θ(Nlog N)2/log log N) or Θ(N(log N)2) or something in between.
# - Best Case Complexity: O(n*log n)
# When the array is already sorted, the total number of comparisons for each interval (or increment) is equal to the size of the array.
# - Average Case Complexity: O(n*log n)
# It is around O(n^1.25).
# The complexity depends on the interval chosen. The above complexities differ for different increment sequences chosen. Best increment sequence is unknown.
# 2. Space Complexity:
# - The space complexity for shell sort is O(1).