def maxProfitRec(prices: list[int]) -> int:
    n = len(prices)

    def rec(i: int, holding: bool):
        if i == n:
            return 0
        if holding:  # we bought before already so we can 1) sell it 2) hold it longer
            sell = prices[i] + rec(i + 1, False)
            hold = rec(i + 1, True)
            return max(sell, hold)
        else:
            # we can buy or do nothing
            buy = -prices[i] + rec(i + 1, True)
            hold = rec(i + 1, False)
            return max(buy, hold)

    return rec(0, False)


prices = [1, 2, 3, 4, 5]
print(maxProfitRec(prices))


def maxProfit(prices: list[int]) -> int:
    """
        dp[i][holding] - i'th day, 0 - don't hold stocks, 1 -  hold stocks
        dp[n-1][0] - max profit in the last day

        dp[0][0] - max profit at 1st day without keeping stocks
        dp[0][1] - max profit at 1st day with holding stocks. However, you can buy it then immediately sell it on the same day.

    Find and return the maximum profit you can achieve.

        if I keep stocks at i'th day:
            1. sell them dp[i][0] = dp[i-1][1] + prices[i]
            2. do nothing dp[i][1] = dp[i-1][1]

        else: don't have stocks
            1. buy them  dp[i][1] = dp[i-1][0] - prices[i]
            2. do nothing dp[i][0] = dp[i-1][0]

    """
    n = len(prices)
    dp = [[0, 0] for _ in range(n)]
    dp[0][1] = -prices[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

    return dp[n - 1][0]


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
