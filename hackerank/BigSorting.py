

def pivot(array, low, high):
    pi = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] < pi:
            i +=1
            array[j], array[i] = array[i], array[j]

    array[high], array[i+1] = array[i+1], array[high]
    return i+1

def quicksort(array, low, high):
    if low < high:


        pi = pivot(array,low,high)

        quicksort(array,low, pi - 1)
        quicksort(array, pi+1, high)



arr = ["10", "7", "8", "9", "1", "5"]
result = list(map(int, arr))
n = len(result)
quicksort(result, 0, n - 1)
print(list(map(str,result)))


#or the optimal one and the better

def bigSorting(unsorted):
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted

