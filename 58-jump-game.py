def canJump(nums: list[int]) -> bool:
    n = len(nums)
    dp = [False for _ in range(n)]
    dp[0] = True
    for i in range(n):
        k = nums[i]
        # dp[i] means we jumped here somehow before, so we can jump from here as well
        while dp[i] and k > 0:
            jump = i + k
            if jump >= n - 1:
                return True
            dp[jump] = True
            k -= 1
    return dp[-1]


nums = [2, 0]
print(canJump(nums))
