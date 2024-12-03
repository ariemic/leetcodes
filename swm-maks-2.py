# Dane są dwie tablice liczb całkowitych. Napisz funkcję która przyjmuje dwie tablice i znajduje dwie liczby (jedną z tablicy A, drugą z tablicy B ) z najmniejszą odległością (najmniejszą nieujemną różnicą).
# Kurde to jest medium z leetcode'a czyli 1 rozmowa -> easy, 2nd -> mid (trzeba robić zadanka)


def findSmallestDifference(A, B):
    A.sort()
    B.sort()
    # print(A)
    # print(B)
    i, j = 0, 0
    res = -1
    mini = float("inf")
    while i < len(A) and j < len(B):
        # always move pointer indicating smaller element
        diff = abs(A[i] - B[j])
        if diff == 0:
            return (A[i], B[j])
        if diff < mini:
            mini = diff
            res = (A[i], B[j])

        if A[i] < B[j]:
            i += 1  # reduce the distance between elements
        else:
            j += 1

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
