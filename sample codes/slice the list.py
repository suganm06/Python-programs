def perform_operations(test_case):
    N, L = test_case
    L = list(map(int, L.split()))

    reversed_list = list(reversed(L))
    print(" ".join(map(str, reversed_list)))

    every_third_with_addition = [str(L[i] + 3) for i in range(3, N, 3)]
    print(" ".join(every_third_with_addition))

    every_fifth_with_subtraction = [str(L[i] - 7) for i in range(5, N, 5)]
    print(" ".join(every_fifth_with_subtraction))

    sum_between_indices = sum(L[3:8])
    print(sum_between_indices)

T = int(input())
for _ in range(T):
    N = int(input())
    L = input()
    test_case = (N, L)
    perform_operations(test_case)