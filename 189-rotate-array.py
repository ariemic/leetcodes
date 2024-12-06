def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n < 2: return

    def rec(i: int, value: int, end: int):
        if i == end:
            nums[i] = value
            return
        nextHop = (i + k) % n
        rec(nextHop, nums[i], end)
        nums[i] = value

    rec(k%n, nums[0], 0)
    if k % n == 0 or (n % k == 0 and k != 1):
        rec((k + 1)%n, nums[1], 1)


# arr = [1, 2, 3, 4, 5, 6, 7]
# rotate(arr, 3)
# print(arr)

arr = [1, 2]
rotate(arr, 1)
print(arr)
