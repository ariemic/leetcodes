def merge(nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    k = 0
    for i in range(m + n):
        if nums2[k] < nums1[i] or nums1[i] == 0:
            nums1[m + k], nums1[i] = nums1[i], nums2[k]
            k += 1
        
        

nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
merge(nums1, m, nums2, n)
print(nums1)