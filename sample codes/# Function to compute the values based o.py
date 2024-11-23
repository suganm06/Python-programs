def compute_values(n):
    result = []
    for i in range(n):
        if i == 0:
            result.append(3)
        elif i % 2 == 0:
            result.append(2 * i)
        else:
            result.append(i * i)
    return result

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        values = compute_values(n)
        print(*values)

if __name__ == "__main__":
    main()