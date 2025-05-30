import time
import random

def createRandomArray(size):
    array = list(range(1,size+1))
    random.shuffle(array)
    return array

smallA = createRandomArray(150)
midA = createRandomArray(5600)
bigA = createRandomArray(35000)

# ------Insertion Sort ------#
def insertion_sort(Array):
    i = 1
    while i < len(Array):
        j = i
        while j > 0 and Array[j-1] > Array[j]:
            Array[j],Array[j-1] = Array[j-1], Array[j]
            j = j-1
        i = i+1

# ------Heap Sort ------#
def heapify(Array, n, i):
    mayor = i
    izq = 2*i+1
    der = 2*i+2

    if izq < n and Array[izq] > Array[mayor]:
        mayor = izq
    if der < n and Array[der] > Array[mayor]:
        mayor = der

    if mayor != i:
        Array[i], Array[mayor] = Array[mayor], Array[i]
        heapify(Array,n,mayor)

def heap_sort(Array):
    n = len(Array)
    for i in range(n//2-1,-1,-1):
        heapify(Array,n,i)
    for i in range(n-1,0,-1):
        Array[0],Array[i] = Array[i], Array[0]
        heapify(Array,i,0)

# ------Quick Sort ------#
def partition(array, bajo, alto):
    pivot = array[alto]
    i = bajo-1

    for j in range(bajo, alto):
        if array[j] < pivot:
            i+=1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[alto] = array[alto],array[i+1]
    return i+1

def quick_sort(array, bajo, alto):
    if bajo < alto:
        part = partition(array,bajo,alto)
        quick_sort(array,bajo,part-1)
        quick_sort(array,part+1,alto)

# ------Merge Sort ------#
def merge(array, izq, med, der):
    n1 = med - izq + 1
    n2 = der - med

    L = [0] * n1
    R = [0] * n2

    for i in range (n1):
        L[i] = array[izq+i]
    for j in range(n2):
        R[j] = array[med+1+j]

    i = 0
    j=0
    k = izq

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i<n1:
        array[k] = L[i]
        i += 1
        k += 1
    while i<n2:
        array[k] = R[j]
        j += 1
        k += 1

def merge_sort(array, izq, der):
    if izq < der:
        med = (izq+der) // 2

        merge_sort(array,izq,med)
        merge_sort(array, med+1, der)
        merge(array, izq, med, der)

# ------Selection Sort ------#
def selection_sort(array):
    n=len(array)
    for i in range(n-1):
        min = i

        for j in range(i+1, n):
            if array[j] < array[min]:
                min = j

        array[i], array[min] = array[min], array[i]

# ------Bubble Sort ------#
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if (swapped == False):
            break

start = 0
end = 0


start = time.time()
heap_sort(smallA)
end = time.time()
print(end-start)

start = time.time()
heap_sort(midA)
end = time.time()
print(end-start)

start = time.time()
heap_sort(bigA)
end = time.time()
print(end-start)