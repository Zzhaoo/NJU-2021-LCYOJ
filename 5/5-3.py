"""
硬币最小数量
"""
class Solution:
    def solute(self, target: int, coins: list):
        res = target + 1
        dp = [[target + 1]*(target+1) for i in range(len(coins))]
        for j in range(0, target + 1):
            if j % coins[0] == 0:
                dp[0][j] = j // coins[0]
        for i in range(1, len(coins)):
            for j in range(target + 1):
                count_1 = dp[i - 1][j - coins[i]] if j >= coins[i] else target
                count_2 = dp[i][j - coins[i]] if j > coins[i] else target
                dp[i][j] = min(min(count_1, count_2) + 1, dp[i - 1][j])
                if j == target:
                    res = min(res, dp[i][j])
        if res == target + 1:
            return -1
        return res

if __name__ == "__main__":
    s = Solution()
    for _ in range(int(input())):
        coin_num, target = map(int, input().split())
        coins = [int(value) for value in input().split()]
        print(s.solute(target, coins))