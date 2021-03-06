#! /usr/bin/env python3

import time
import matplotlib.pyplot as plt


def heap_sort(arr):
    """ Implementation of the heap sort algorithm.

    :param arr:
    :return:

    # List with an even number ob items to function call.
    >>> heap_sort([0, -1, 5, -2])
    [-2, -1, 0, 5]

    # List with an uneven number of items to function call.
    >>> heap_sort([3, 2, 0, 4, 1])
    [0, 1, 2, 3, 4]

    # List with only one element to function call.
    >>> heap_sort([0])
    [0]

    # Empty list to function call.
    >>> heap_sort([])
    []
    """
    # # Option #1:
    # root_parent_index = 0
    # last_child_index = len(array) - 1
    # # initial heapify operation.
    # heapify(array)
    # for child_index in range(last_child_index, root_parent_index, -1):
    #     # Swap the last item with the first item.
    #     array[root_parent_index], array[child_index] = array[child_index], array[root_parent_index]
    #     # Repair heap from bottom up.
    #     repair_heap(array, root_parent_index, child_index - 1)

    # Option #2:
    first_idx = 0
    first_child_idx = 1
    last_child_idx = len(arr) - 1

    heapify(arr)

    for last_idx in reversed(range(first_child_idx, last_child_idx + 1)):
        arr[first_idx], arr[last_idx] = arr[last_idx], arr[first_idx]
        repair_heap(arr, first_idx, last_idx - 1)

    return arr


def heapify(arr):
    """

    :param arr:
    :return:

    # List with an even number of elements to function call.
    >>> heapify([0, 1, 2, 3, 4, 5])
    [5, 4, 2, 3, 1, 0]

    # List with an uneven number of elements to function call.
    >>> heapify([0, 1, 2])
    [2, 1, 0]

    # List with only 1 element to function call.
    >>> heapify([0])
    [0]

    # Empty list to function call.
    >>> heapify([])
    []

    """
    # # Option #1:
    # last_child_index = len(array) - 1
    # last_parent_index = (last_child_index - 1) // 2
    #
    # for parent_index in range(last_parent_index, -1, -1):
    #     repair_heap(array, parent_index, last_child_index)

    # Option #2:
    if arr:
        last_child = len(arr) - 1
        last_parent = (last_child - 1) >> 1  # parent = (child - 1) // 2
        if (last_child % 2) == 0:
            right = last_child
            left = right - 1
            if arr[right] > arr[left] and arr[right] > arr[last_parent]:
                arr[right], arr[last_parent] = arr[last_parent], arr[right]
            elif arr[left] > arr[right] and arr[left] > arr[last_parent]:
                arr[left], arr[last_parent] = arr[last_parent], arr[left]
        else:
            left = last_child
            if arr[left] > arr[last_parent]:
                arr[left], arr[last_parent] = arr[last_parent], arr[left]

        for parent in range(last_parent - 1, -1, -1):
            left = (parent << 1) + 1  # left = (2 * parent) + 1
            right = left + 1
            if arr[left] > arr[right] and arr[left] > arr[parent]:
                arr[left], arr[parent] = arr[parent], arr[left]
                repair_heap(arr, left, last_child)
            elif arr[right] > arr[left] and arr[right] > arr[parent]:
                arr[right], arr[parent] = arr[parent], arr[right]
                repair_heap(arr, right, last_child)

    return arr


def repair_heap(arr, parent_index, last_child_index):
    """ Repair the heap.

    :param arr:
    :param parent_index:
    :param last_child_index:
    :return:

    >>> invalid_heap = [3, 2, 0, 4, 1]
    >>> repair_heap(invalid_heap, 1, 4)
    [3, 4, 0, 2, 1]
    >>> repair_heap(invalid_heap, 0, 4)
    [4, 3, 0, 2, 1]

    """
    # # Option #1:
    # current_parent_index = parent_index
    # heap_size = last_child_index + 1
    #
    # while current_parent_index < heap_size:
    #     left_child_index = 2 * current_parent_index + 1
    #     right_child_index = left_child_index + 1
    #     max_child_index = left_child_index
    #     if left_child_index > last_child_index:
    #         break
    #     if right_child_index < heap_size and array[right_child_index] > array[left_child_index]:
    #         max_child_index = right_child_index
    #     if array[max_child_index] > array[current_parent_index]:
    #         array[max_child_index], array[current_parent_index] = array[current_parent_index], array[max_child_index]
    #         current_parent_index = max_child_index
    #     else:
    #         break

    # Option #2:
    import math

    current_depth = int(math.log2(parent_index + 1))
    max_depth = int(math.log2(last_child_index + 1))
    parent = parent_index

    for depth in range(current_depth, max_depth):
        left = (parent << 1) + 1
        right = left + 1
        if right <= last_child_index:
            if arr[left] > arr[right] and arr[left] > arr[parent]:
                arr[left], arr[parent] = arr[parent], arr[left]
                parent = left
            elif arr[right] > arr[left] and arr[right] > arr[parent]:
                arr[right], arr[parent] = arr[parent], arr[right]
                parent = right
        elif left <= last_child_index:
            if arr[left] > arr[parent]:
                arr[left], arr[parent] = arr[parent], arr[left]
        else:
            break

    return arr


def runtime_plot():
    """ Generate runtime plot T(n) with different input sizes of n.
    """

    print("Start runtime plot")
    for count_n in range(1000, 101000, 1000):
        arr = [x for x in range(count_n, 0, -1)]
        time_milli = measure_time(arr)
        plt.plot(count_n, time_milli, 'o')
    plt.xlabel("count n of elements")
    plt.ylabel("runtime T(n) in milliseconds")
    plt.show()
    print("Finish runtime plot")


def measure_time(arr):
    """ Measure time consumption of sorting algorithm for given array in milliseconds.
    """

    start = time.perf_counter()
    heap_sort(arr)
    end = time.perf_counter()
    return (end - start) * 1000


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    runtime_plot()

    array = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]
    print("Array before sorting:", array)
    time_micro = measure_time(array) * 1000
    print("Runtime T(n) = {0:e} microseconds".format(time_micro))
    print("Array after sorting:", array)
