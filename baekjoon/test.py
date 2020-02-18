row, col = 3, 4
D = 5




for i in range(1, 2 * D, 2):
    for j in range(-(i//2), i//2 + 1, 1):
        print("[", row + abs(i//2 - j), "]", "[", col - j, "]", end=" ")
    print()