"""
无重复字符子集
"""


class Solution:
    def solute(self, arr: list, covered: list) -> int:
        if len(arr) <= 0:
            return 0
        num = arr[0]
        covered_new = list(covered)
        while num != 0:
            remainder = num % 10
            num = int(num / 10)
            if covered[remainder] == 1:
                return self.solute(arr[1:], covered)
            covered_new[remainder] = 1
        return max(arr[0] + self.solute(arr[1:], covered_new), self.solute(arr[1:], covered))


if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        _ = int(input())
        covered = [0] * 10
        num = s.solute([int(num) for num in input().split()], covered)
        print(num)
