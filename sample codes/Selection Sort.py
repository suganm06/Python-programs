def selectionSort(list1, n):
	for s in range(n):
		min_idx = s
		for i in range(s + 1, n):
			if list1[i] < list1[min_idx]:
				min_idx = i
		(list1[s], list1[min_idx]) = (list1[min_idx], list1[s])

n=int(input("list size:"))
list1 = []
for i in range(0,n):
    item = int(input())
    list1.append(item)
    
print("The unsorted list is:", list1)
selectionSort(list1, n)
print("The sorted new list is:",list1)