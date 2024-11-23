def main():
    T = int(input())
    for _ in range(T):
        s = input()
        if s.startswith("@"):
            s = s[1:]
            lengths = [str(len(word)) for word in s.split()]
            result = ",".join(lengths)
            print(result)

main()