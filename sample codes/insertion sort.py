n=int(input("list size:"))
list1 = []
for i in range(0,n):
    item = int(input())
    list1.append(item)
        
def insertion_sort(list1):
		for i in range(1, n):
			a = list1[i]
			j = i - 1
			while j >= 0 and a < list1[j]:
				list1[j + 1] = list1[j]
				j -= 1
			list1[j + 1] = a
		return list1

print("The unsorted list is:", list1)
print("The sorted new list is:", insertion_sort(list1))