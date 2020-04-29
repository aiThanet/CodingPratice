# Sorting Algorithm

## Sorting Terminology

### In-place sorting
An in-place sorting algorithm uses constant extra space for producing output
(modifies the given array only) ex. Insertion Sort and Selection Sorts

### Internal and External Sorting
For large amount of data, which can not store in memory at a time, this sorting is called `external sorting`. (Merge Sort and its variations are typically used for external sorting).  When all data is stored in memory, then sorting is called `internal sorting`

### stable sorting
A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output.
![stable defination](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-8e99a78816d6dccaf01441f612788157_l3.svg)

## Time and space complexity
![time&spaceComplexity](time.png)

1. `Selection Sort`
Sort an array by repeatedly finding the minimum element from unsorted part and putting it at the beginning.
- Time Complexity: O(n<sup>2</sup>)
- Auxiliary Space: O(1)
- O(n) swaps, useful when memory write is a costly operation
- Stable
- In-place

2. `Merge Sort`
is a Divide and Conquer algorithm. It divides input array in two halves, calls itself on the two halves and then merges the two sorted halves.
- Time Complexity: T(n) = 2T(n/2) + O(n). It falls in case II of Master Method and solution of the recurrence is O(nLogn)
- Auxiliary Space: O(n)
- Not In-place in a typical implementation
- Stable
-
3. `Quick Sort`
is a Divide and Conquer algorithm. It selects an element as a pivot and partitions the given array around the pivot.
- Time Complexity: T(n) = T(k) + T(n-k-1) + O(n)
- Worst Case: occurs when pick the greastest or smallest element as pivot: T(n) = T(n-1) + O(n) which is O(n<sup>2</sup>)
- Best Case: occurs when always pick the middle element as pivot: T(n) = 2T(n/2) + O(n) which is O(nLogn)
- Average Case: O(nLogn)
- Although the worst case time is O(n<sup>2</sup>). In general, QuickSort is faster in practice because its inner loop can be efficiently implemented on most architecture and most real-world data. Howevert, mergeSort is generally considered better when data is huge and stored in external storage.
- Can be stable and unstable depend on implementaion
- In-place

4. `Insertion Sort` is a simple sorting algorithm which select a element from unsorted input and insert it into sorted output in ascending order.
- Time Complexity: O(n<sup>2</sup>)
- Auxiliary Space: O(1)
- Worst Case: elements are sorted in reverse order.
- Base Case: elements are already sorted
- Uses: when number of input is small and only few elements are misplaced.