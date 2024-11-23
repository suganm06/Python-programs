def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        for _ in range(8):  # Loop exactly 8 times for 8 bits
            bit = (N >> 7) & 1  # Extract the leftmost bit
            print(bit, end="")
            N <<= 1  # Shift N to the left
        print()

main()