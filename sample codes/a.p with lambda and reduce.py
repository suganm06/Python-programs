from functools import reduce

def generate_AP(a1, d, n):
    ap_series = [a1 + (i * d) for i in range(n)]
    return ap_series

T = int(input())

for _ in range(T):
    a1, d, n = map(int, input().split())

    ap_series = generate_AP(a1, d, n)

    print(" ".join(map(str, ap_series)))

    squares = list(map(lambda x: x**2, ap_series))
 
    print(" ".join(map(str, squares)))

    sum_of_squares = reduce(lambda x, y: x + y, squares)

    print(sum_of_squares)