"""
购买蔬菜

spand(i) = min(a + spand(i-1, 100), b+ spand(i-1, 010), c+ spand(i-1, 001)


"""
class Solution:
    def solute(self, sales: list):
        n = len(sales)
        dp = [[0]*3 for _ in range(n)]
        for i in range(n):
            for j in range(3):
                if i == 0:
                    dp[i][j] = min(sales[i][j-1], sales[i][j-2])
                    continue
                dp[i][j] = min(sales[i][j - 1] + dp[i-1][j - 1], sales[i][j - 2] + dp[i-1][j - 2])
        print(min(dp[-1]))

if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        sales = []
        m = int(input())
        for _ in range(m):
            sale = [int(num) for num in input().split()]
            sales.append(sale)
        s.solute(sales)
