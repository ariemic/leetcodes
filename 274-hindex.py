def hIndex(citations: list[int]) -> int:
    n = len(citations)
    dp = [0 for _ in range(n + 1)]

    for num in citations:
        if num <= n:
            dp[num] += 1
        else:
            dp[n] += 1

    for i in range(n, -1, -1):
        if dp[i] >= i:
            return i
        else:
            if i > 0:
                dp[i - 1] += dp[i]


# citations = [3, 0, 6, 1, 5]
citations = [0]
print(hIndex(citations))
