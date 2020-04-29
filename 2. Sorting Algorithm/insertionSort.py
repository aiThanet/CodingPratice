
def insertion_sort(arr):
    for i in range(1,len(arr)):
        insert_ele = arr[i]
        
        j = i-1
        while j >= 0 and arr[j] > insert_ele:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = insert_ele

        
   
if __name__ == '__main__':
    arr = [4,3,2,10,12,1,5,6]
    print('Given array is', arr)
    insertion_sort(arr)
    print('Sorted array is', arr)

    arr = [2,33,18,13,5,45]
    print('Given array is', arr)
    insertion_sort(arr)
    print('Sorted array is', arr)