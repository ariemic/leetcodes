#todo napisz jeszcze raz z O(n+m)

def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    k = 0
    if n == 0:
        return
    for i in range(m + n):
        if k > n - 1:
            return
        if nums2[k] < nums1[i] or (i - k >= m and nums1[i] == 0):
            for j in range(m + n - 1, i, -1):
                nums1[j] = nums1[j - 1]
            nums1[i] = nums2[k]
            print(nums1)
            k += 1
    return


# nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)
