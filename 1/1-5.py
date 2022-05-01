"""
arr = [1, 2, 3, 4, 5, 6...n]

f(1, 1) = arr[0]
f(2, 1) = arr[0] + arr[1]
...
f(n, 1) = arr[0] + arr[1] + ... + arr[n-1]

f(1, 2) = -1
f(2, 2) = min(
            max(f(1, 1), arr[1])
            )
f(3, 2) = min(
            max(f(1, 1), arr[1] + arr[2]),
            max(f(2, 1), arr[2])
            )
...
f(n, 2) = min(
            max(f(1, 1), arr[1] + ... + arr[n-1]),
            ...
            max(f(n-1, 1), arr[n-1])
            )

...
f(j, i)
f(n, m) = min(
            max(f(m-1, m-1), arr[m-1] + arr[m] + ... + arr[n-1]),
            max(f(m, m-1), arr[m] + arr[m+1] + ... + arr[n-1]),
            max(f(m+1, m-1), arr[m+1] + arr[m+2] + ... + arr[n-1]),
            ...
            max(f(n-1, m-1), a[n-1])
            )
"""
class Solution:
    def solute(self, n: int, arr: list, m: int):
        dp = []
        for i in range(m):
            dp.append([])
            for j in range(n):
                dp[i].append(-1)
        dp[0][0] = arr[0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + arr[j]
        for i in range(1, m):
            for j in range(i, n):
                dp[i][j] = min([max(dp[i-1][x], sum(arr[x+1:j+1])) for x in range(i-1, j)])
        print(dp[m-1][n-1])


if __name__ == "__main__":
    s = Solution()
    t = int(input())
    for i in range(t):
        m, n = tuple([int(tmp) for tmp in input().split()])
        m = min(m, n)
        arr = [int(p) for p in input().split()]
        s.solute(n, arr, m)
