




def merge(arr, lefthalf, righthalf):
    i = j = k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        else:
            arr[k] = righthalf[j]
            j += 1
            k += 1

    while i < len(lefthalf):
        arr[k] =  lefthalf[i]
        i += 1
        k += 1
    
    while j < len(righthalf):
        arr[k] = righthalf[j]
        j += 1
        k += 1

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(arr, lefthalf, righthalf)
    return arr


arr = [2, 5, 8, 33, 22, 1, 9, 11]
print("mergeSorted array is", mergeSort(arr))