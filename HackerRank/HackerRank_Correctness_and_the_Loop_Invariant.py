#Insertion sort problem

def insertion_sort(l):
    for i in range(1, len(l)): #because the constraint is 1 <= s <= 1000
        j = i-1
        key = l[i]
        while (j > -1) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
    return l

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))

