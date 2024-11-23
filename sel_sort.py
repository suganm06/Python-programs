a = [56,7,8,70,0,4]
for i in range(0,4):
    min_val = min(a[i:])
    min_index = a.index(min_val)
    a[i],a[min_index] = a[min_index],a[i]
print(a)