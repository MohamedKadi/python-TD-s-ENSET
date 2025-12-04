def rechercher(array, V):
    n = len(array)
    low = 0
    high = n-1
    
    while(low <= high):
        mid = (high+low) // 2
        if array[mid] < V:
            low = mid+1
        elif  array[mid] > V:
            high = mid-1
        else:
            return mid
    return -1

def introTutorial(V, arr):
    arr.sort()
    return rechercher(arr,V)

list = [1,2,3,5,10,20,-10]
print(introTutorial(3, list))
print(list)

