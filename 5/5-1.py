"""
格子里的整数
"""


class Solution:
    def __init__(self):
        self.direct_x = [-1, 0, 1, 0]
        self.direct_y = [0, 1, 0, -1]

    def dfs(self, path: list, metrix: list, metrix_passed: list, x: int, y: int) -> int:
        min_cost = 99999
        if x == -1 or x == len(metrix) or y == -1 or y == len(metrix) or metrix_passed[x][y] == 1:
            return min_cost
        path.append(metrix[x][y])
        metrix_passed[x][y] = 1
        if x == len(metrix) - 1 and y == len(metrix) - 1:
            min_cost = sum(path)
        else:
            for i in range(4):
                min_cost = min(self.dfs(path, metrix, metrix_passed, x + self.direct_x[i], y + self.direct_y[i]),
                               min_cost)
        path.pop()
        metrix_passed[x][y] = 0
        return min_cost

    def solute(self, metrix: list):
        path = []
        metrix_passed = [[0] * len(metrix) for _ in range(len(metrix))]
        cost = self.dfs(path, metrix, metrix_passed, 0, 0)
        print(cost)


if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        size = int(input())
        arr = [int(num) for num in input().split()]
        metrix = []
        for i in range(size):
            metrix.append(arr[0 + i * size: size + i * size])
        s.solute(metrix)
