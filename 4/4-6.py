"""
按照要求保留数组元素使得和最大
"""
class Solution:
    def solute(self, arr, n):
        dp = [0] * 21
        for i in range(n):
            dp[arr[i]] += 1
        s = 0
        for i in range(20, -1, -1):
            if(dp[i] > 0):
                s += i * dp[i]
                dp[i - 1] -= dp[i]
        return s


if __name__ == "__main__":
    s = Solution()
    for _ in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        print(s.solute(nums, n))