def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(arr,L,R)

def merge(arr,L,R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    if i < len(L):
        arr[k:] = L[i:]
    if j < len(R):
        arr[k:] = R[j:]

if __name__ == '__main__':
    arr = [12,11,13,5,6,]
    print('Given array is', arr)
    merge_sort(arr)
    print('Sorted array is', arr)

    arr = [2,33,18,13,5,45]
    print('Given array is', arr)
    merge_sort(arr)
    print('Sorted array is', arr)