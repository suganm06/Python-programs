a=int(input())
s=0
for i in range(1,a):
    r=a%i
    if(r==0):
        s+=i
        
if(a==s):
    print("perfect number")
else:
    print("not a perfect number")