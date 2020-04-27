import sys

def selection_sort(ls):
    for i in range(len(ls)):
        min_idx = i
        for j in range(i,len(ls)):
            if ls[j] < ls[min_idx]:
                min_idx = j
        ls[i],ls[min_idx] = ls[min_idx],ls[i]
    return ls


A = [60,26,12,22,10]

print(selection_sort(A))