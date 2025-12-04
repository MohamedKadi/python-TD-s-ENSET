#print each time you shift

"""
5
2 4 6 8 3
output:
2 4 6 8 8 
2 4 6 6 8 
2 4 4 6 8 
2 3 4 6 8 
"""


def insertionSort1(n, arr):
    max = n-1
    last = arr[max]
    while max > 0 and arr[max - 1] > last:
        arr[max] = arr[max - 1]
        print(*arr)
        max -= 1
    arr[max] = last
    print(*arr)

insertionSort1(5, [2, 4, 6, 8, 0])