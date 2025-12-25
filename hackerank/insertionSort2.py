#print each time you shift

"""
7
3 4 7 5 6 2 1
output:
3 4 7 5 6 2 1
3 4 7 5 6 2 1
3 4 5 7 6 2 1
3 4 5 6 7 2 1
2 3 4 5 6 7 1
1 2 3 4 5 6 7
"""


def insertionSort1(n, arr):
    max = n-1 #0
    last = arr[max] #1
    while max > 0 and arr[max - 1] > last:
        arr[max] = arr[max - 1]
        max -= 1
    arr[max] = last

def insertionSort2(n,arr):
    for i in range(1,n):
        insertionSort1(i+1,arr)
        print(*arr)



insertionSort2(8, [8 ,7 ,6 ,5 ,4 ,3 ,2 ,1])