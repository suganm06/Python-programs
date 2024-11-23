def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

n=int(input("list size:"))
list1 = []
for i in range(0,n):
    item = int(input())
    list1.append(item)

print("The unsorted list is:", list1)
bubbleSort(list1)
print("The sorted new list is:",list1)