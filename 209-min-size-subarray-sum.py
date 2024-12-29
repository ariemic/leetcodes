# O(n) - time complexity
def minSubArrayLen(target: int, nums: list[int]) -> int:
    if sum(nums) < target:
        return 0
    cur_sum = 0
    min_leng = float("inf")
    left = 0

    for right in range(len(nums)):
        cur_sum += nums[right]

        while cur_sum >= target:
            if right - left + 1 < min_leng:
                min_leng = right - left + 1
                print(nums[left : right + 1])

            cur_sum -= nums[left]
            left += 1

    return min_leng


nums = [2, 3, 4, 3, 1, 2]
target = 7
print(minSubArrayLen(target, nums))


# O(nlogN) - time complexity
# O(n) - space complexity
def minSubArrayLenDynamic(target: int, nums: list[int]) -> int:
    from bisect import bisect_left

    n = len(nums)
    prefix = [0] * (n + 1)

    # Calculate prefix sums
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    min_len = float("inf")

    # Binary search for the minimal subarray length
    for i in range(n):
        # To find a subarray starting at index i with sum >= target:
        # sum(i, j) = prefix[j + 1] - prefix[i]
        # We need sum(i, j) >= target, so:
        # prefix[j + 1] >= target + prefix[i]
        required_sum = target + prefix[i]
        j = bisect_left(prefix, required_sum)
        if j <= n:
            min_len = min(min_len, j - i)

    return min_len if min_len != float("inf") else 0
