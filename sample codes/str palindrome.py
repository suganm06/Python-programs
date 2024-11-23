def palindrome(s):
    s1=s.lower()
    rev_s=reversed(s1)
    return rev_s,s1

def main():
    T = int(input())
    for _ in range(T):
        s = input()
        rev_s,s1 = palindrome(s)
        if list(s1)==list(rev_s):
            print("It is a palindrome")
        else:
            print("It is not a palindrome")
 
main()