def removeElement(nums, val):
    """
    1. two pointers or for and using k to subtract from n
    k - amount of numbers that aren't equal to val
    """
    n = len(nums)

    # works when array contains at least one element different than val
    left, right = 0, n - 1
    k = 0
    while left < right:
        if nums[left] != val:
            k += 1
            left += 1
        elif nums[right] == val:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            k += 1  # right is different than val
            right -= 1
            left += 1
    if left == right and nums[left] != val:
        k += 1

    return nums[:k]


nums = [1]
val = 1
print(removeElement(nums, val))

nums2 = [3, 3, 3, 3]
val2 = 3
print(removeElement(nums2, val2))


nums3 = [3, 2, 2, 3]
val3 = 3
print(removeElement(nums3, val3))
