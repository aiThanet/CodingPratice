def quick_sort(arr,low,high):
    if low < high:
        pivot = partition(arr,low,high)
        quick_sort(arr,low,pivot-1)
        quick_sort(arr,pivot,high)

def partition(arr,low,high):
    # pivot is last element
    pivot = arr[high]

    i = low-1
    for j in range(low,high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[high], arr[i+1] = arr[i+1], arr[high]
    return (i+1)

if __name__ == '__main__':
    arr = [12,11,13,5,6,]
    print('Given array is', arr)
    quick_sort(arr,0,len(arr)-1)
    print('Sorted array is', arr)

    arr = [2,33,18,13,5,45]
    print('Given array is', arr)
    quick_sort(arr,0,len(arr)-1)
    print('Sorted array is', arr)

