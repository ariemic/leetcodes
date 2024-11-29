# Masz dwie tablice, w każdej są unikalne wartości. Znajdz i zwróć najmniejszy element element o tej samej wartości występujący w obu tablicach
# tak aby suma indexów tych elementów była jak najmniejsza. Jest wiele elementów które się powtarzają w obu tablicach.


def findSmallestIndexSum(nums1, nums2):
    mini = float("inf")
    val = None
    hashmap = {}
    n, m = len(nums1), len(nums2)

    if n < 1 or m < 1:
        return

    for i in range(n):
        hashmap[nums1[i]] = i
    print(hashmap)

    for i in range(m):
        if nums2[i] in hashmap:
            if mini > i + hashmap[nums2[i]]:
                mini = i + hashmap[nums2[i]]
                val = nums2[i]

    return val, mini


nums1 = [1, 2, 5, 8, 9]
nums2 = [9, 8, 2, 7, 1, 5]

print(findSmallestIndexSum(nums1, nums2))
