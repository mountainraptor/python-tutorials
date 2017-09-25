# Implementation of heap sort

# Heapify a subtree rooted at index i
def heapify(lst, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * (i + 1)

    if l < n and lst[i] < lst[l]:
        largest = l

    if r < n and lst[largest] < lst[r]:
        largest = r

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)

def heapsort(lst):
    n = len(lst)

    for i in range(n, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)
    return lst
