def heapify(array, i, size):
    largest = i
    left = (2*i+1)
    right = (2*i+2)
    if left < size and array[left] > array[i]:
        largest = left
    if right < size and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, largest, size)
def Heap_Sort(array):
    size = len(array)
    for i in range(size//2, -1, -1):
        heapify(array, i, size)
    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)

data = [10, 3, 76, 34, 23, 32]
print("Heap Sort: ")
Heap_Sort(data)
print(data)