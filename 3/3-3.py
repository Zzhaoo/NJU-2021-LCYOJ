"""
子矩阵问题
"""
class Solution:
    def maximalRectangle(self, matrix: list) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        left = [[0] * n for _ in range(m)]
        # init matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    left[i][j] = 1 if j == 0 else left[i][j-1] + 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                width = left[i][j]
                area = width
                # right
                for k in range(i-1, -1, -1):
                    width = min(width, left[k][j])
                    area = max(area, (i - k + 1) * width)
                ans = max(ans, area)
        return ans


if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        m, n = map(int, input().split())
        nums = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            row = list(map(int, input().split()))
            for j in range(n):
                nums[i][j] = row[j]
        print(s.maximalRectangle(nums))

