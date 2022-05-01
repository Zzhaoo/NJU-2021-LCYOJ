"""
最小化初始点
"""


class Solution:
    def solute(self, arr: list, row: int, col: int):
        metrix = []
        dp = []
        for i in range(row):
            tmp = arr[0 + i * col:col + i * col]
            metrix.append(tmp)
            dp.append([0] * col)
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                dp_down = dp[i + 1][j] if (i + 1) < row else 31
                dp_right = dp[i][j + 1] if (j + 1) < col else 31
                # dp[-1][-1]
                if dp_right == 31 and dp_down == 31:
                    dp[i][j] = max(0, -metrix[i][j]) + 1
                else:
                    dp[i][j] = max((min(dp_down, dp_right) - metrix[i][j]), 1)
        print(dp[0][0])


if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        row, col = map(int, input().split())
        arr = [int(num) for num in input().split()]
        s.solute(arr, row, col)
