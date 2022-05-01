"""
序号乘方
"""


class Solution:
    def solute(self, n):
        cur = 1
        while n >= cur**2:
            n -= cur**2
            cur += 1
        return cur - 1


if __name__ == "__main__":
    s = Solution()
    t = int(input())
    for _ in range(int(input())):
        print(s.solute(int(input())))
