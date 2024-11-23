list  =  [2,4,5,8,3,0]
n  = int(input("Enter the Element to Search:"))
for i in range(len(list)):
      if list[i]==n:
            print("{} is found in {} position".format(n,i))
            break
else:
      print("Not Found")