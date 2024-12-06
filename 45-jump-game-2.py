def jump(nums: list[int]) -> int:
    # dp[i] - min numbers of jumps to get into i
    n = len(nums)
    dp = [float("inf") for _ in range(n)]
    dp[0] = 0
    for i in range(n):
        k = nums[i]
        while k > 0:
            jump = min(i + k, n - 1)
            dp[jump] = min(dp[jump], dp[i] + 1)
            k -= 1
    return dp[-1]


nums = [2, 3, 1, 1, 4]
print(jump(nums))
