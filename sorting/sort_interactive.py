# Sort a user provided list

from merge_sort import mergesort
from quick_sort import quicksort
from heap_sort import heapsort
from bubble_sort import bubblesort

# Check if input is an int
def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print "Enter integers separated by a comma (e.g. 1,3,4,6)\n"
user_input = raw_input("Enter Numbers: ")

input_list = [ int(x.strip()) for x in user_input.split(',') if(represents_int(x)) ]
print "You entered: " + str(input_list)
print "merge sort: " + str(mergesort(input_list))
print "quick sort: " + str(quicksort(input_list))
print "heap sort: " + str(heapsort(input_list))
print "bubble sort: " + str(bubblesort(input_list))
