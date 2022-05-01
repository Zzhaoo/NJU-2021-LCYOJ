"""
数组和窗口
"""


class Solution:
    def solute(self, arr: list, size: int):
        res = 0
        index1 = 0
        index2 = 0
        max = []
        while index2 < len(arr):
            while len(max) != 0 and max[-1] < arr[index2]:
                max.pop()
            max.append(arr[index2])
            if index2 - index1 + 1 == size:
                res += max[0]
                if max[0] == arr[index1]:
                    max.pop(0)
                index1 += 1
            index2 += 1
        print(res)


if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        arr = [int(num) for num in input().split()]
        size = int(input())
        s.solute(arr, size)
