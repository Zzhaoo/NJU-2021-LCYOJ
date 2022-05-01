"""
矩阵计算
"""
class Solution:
    def solute(self, n: int):
        C_arr = [0, 0, 1, 1, 1, 0, 1]
        count = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if C_arr[(i % 7 * j % 7) ** 3 % 7] == 1:  # 这样求余防止溢出,
                    count += 1
        return count



if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        print(s.solute(int(input())))