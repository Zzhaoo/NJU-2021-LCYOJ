"""
矩阵计算
"""

N, X, Y = 0, 0, 0
A, B = [], []

d = {}

class Solution:
    def solute(self, cur, i, j):
        if cur == N:
            return 0
        if (cur, i, j) in d:
            return d[(cur, i, j)]

        max_tip = 0
        if i < X:
            max_tip = max([A[cur] + self.solute(cur + 1, i + 1, j), max_tip])
        if j < Y:
            max_tip = max([B[cur] + self.solute(cur + 1, i, j + 1), max_tip])
        d[(cur, i, j)] = max_tip
        return max_tip



if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        N, X, Y = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        d = {}
        print(s.solute(0, 0, 0))