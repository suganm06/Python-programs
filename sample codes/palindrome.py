a=int(input())
s=0
t=a
while t>0:
    r=t%10
    print(r)
    s=(s*10) + r
    print(s)
    t//=10
    print(t)
    
if a==s:
    print(a,'is an palindrome number')
else:
    print(a,'not an palindrome numbern')