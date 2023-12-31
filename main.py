def heapify(array, start, end):
    current = start
    while (current * 2 + 1) < end:
        left_child = current * 2 + 1
        right_child = current * 2 + 2
        if left_child < end and array[current] < array[left_child]:
            current = left_child
        if right_child < end and array[current] < array[right_child]:
            current = right_child
        if current != start:
            swap(array, current, start)
            start = current
        else:
            break

def swap(array, i_one, i_two):
    array[i_one], array[i_two] = array[i_two], array[i_one]

def non_recursive_heapsort(array):
    n = len(array)
    i = (n // 2) - 1
    while i >= 0:
        heapify(array, i, n)
        i -= 1
    i = n - 1
    while i > 0:
        swap(array, i, 0)
        heapify(array, 0, i)
        i -= 1

array = [10, 52, 4, 9, 20, 44, 11, 3, 8, 12]
non_recursive_heapsort(array)
print(array)
