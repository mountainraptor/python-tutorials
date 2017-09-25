# Give a size of a list and test the speed of multiple sorting algorithms
from merge_sort import mergesort
from quick_sort import quicksort
from heap_sort import heapsort
from bubble_sort import bubblesort

import random
import timeit

def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

list_size = raw_input("Enter List Size to test: ")

if represents_int(list_size) and int(list_size) > 0:
    list_size = int(list_size)
else:
    print "not a valid list size"

# Using list comprehension generate random ints
test_list = [random.randint(-10000,10000) for x in range(list_size)]

# Using a decorater to measure time of function with arguments
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrapped_merge = wrapper(mergesort, test_list)
wrapped_quick = wrapper(quicksort, test_list)
wrapped_heap = wrapper(heapsort, test_list)
wrapped_bubble = wrapper(bubblesort, test_list)

print "merge sort: " + str(timeit.timeit(wrapped_merge, number=5))
print "quick sort: " + str(timeit.timeit(wrapped_quick, number=5))
print "heap sort: " + str(timeit.timeit(wrapped_heap, number=5))
print "bubble sort: " + str(timeit.timeit(wrapped_bubble, number=5))
