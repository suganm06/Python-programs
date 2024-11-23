def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        n = pattern(n)
    
def pattern(n):
     for i in range(n,0,-1):
        for j in range(i):
            if j % 5 == 4:
                print("#", end="")
            else:
                print("*", end="")
        print()
                
main()