"""
子数组的取值范围
"""


class Solution:
    def solute(self, arr: list, num: int):
        res = 0
        index1 = 0
        index2 = 0
        win_max = []
        win_min = []
        while index2 < len(arr):
            while len(win_max) != 0 and win_max[-1] < arr[index2]:
                win_max.pop()
            win_max.append(arr[index2])
            while len(win_min) != 0 and win_min[-1] > arr[index2]:
                win_min.pop()
            win_min.append(arr[index2])
            while index1 <= index2 and win_max[0] - win_min[0] > num:
                res += len(arr) - index2
                if arr[index1] == win_min[0]:
                    win_min.pop(0)
                if arr[index1] == win_max[0]:
                    win_max.pop(0)
                index1 += 1
            index2 += 1
        print(res)


if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        arr = [int(num) for num in input().split()]
        num = int(input())
        s.solute(arr, num)
