a=int(input())
s=0
t=a
while t>0:
    r=t%10
    s=s + r**3
    t//=10
    
if a==s:
    print(a,'it is an Armstrong number')
else:
    print(a,'not an armstrong number')