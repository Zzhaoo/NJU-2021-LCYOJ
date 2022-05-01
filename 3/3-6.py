"""
矩阵计算
"""
class Solution:
    def solute(self, n: int):
        odd = 0
        for i in range(n):
            for j in range(n):
                r = ((i+1)*(j+1)) % 7
                r = (r*r*r) % 7
                if r != 1 or r != 5:
                    odd += 1
        print(odd)


if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        s.solute(int(input()))