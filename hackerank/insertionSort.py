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
    while max > 0:
        if(arr[max] < last):
            arr[max+1] = last
            print(str(arr))
            break
        arr[max] = arr[max-1]
        print(arr)
        print(max)
        max -= 1

insertionSort1(5, [2, 4, 6, 8, 3])