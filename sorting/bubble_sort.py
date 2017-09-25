# Implementation of bubble sort
def bubblesort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return lst
