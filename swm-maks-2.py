# Dane są dwie tablice liczb całkowitych. Napisz funkcję która przyjmuje dwie tablice i znajduje dwie liczby (jedną z tablicy A, drugą z tablicy B ) z najmniejszą odległością (najmniejszą nieujemną różnicą).
# Kurde to jest medium z leetcode'a czyli 1 rozmowa -> easy, 2nd -> mid (trzeba robić zadanka)


def findSmallestDifference(A, B):
    A.sort()
    B.sort()
    print(A)
    print(B)
    point_a, point_b = 0, 0
    len_a, len_b = len(A), len(B)
    mini = float("inf")
    res = -1
    last_diff = 0
    # if I find diff = 0 then break
    while point_a < len_a and point_b < len_b:
        diff = abs(A[point_a] - B[point_b])
        i = 0
        while last_diff < diff and last_diff < mini and i < len_b:
            mini = diff
            i += 1
            diff, last_diff = abs(A[point_a] - B[point_b + i]), diff

    return res


# *Przykłady:*
A = [-7, -3, 2, 10, 16]
B = [-20, 3, 12, -5, 20]
# Wynik: (2, 3) — różnica 1
print(findSmallestDifference(A, B))

A = [7, 5, 1, 3]
B = [30, 10, 40, 20]
# Wynik: (7, 10) — różnica 3

print(findSmallestDifference(A, B))
