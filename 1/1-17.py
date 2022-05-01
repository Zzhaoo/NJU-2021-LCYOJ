"""
冒泡排序
"""


class Solution:
    def bobSort(self, arr: list):
        for i in range(1, len(arr)):
            for j in range(len(arr) - i):
                if arr[j] > arr[j + 1]:
                    tmp = arr[j + 1]
                    arr[j + 1] = arr[j]
                    arr[j] = tmp
        print(" ".join([str(num) for num in arr]))


if __name__ == "__main__":
    s = Solution()
    n = int(input())
    for _ in range(n):
        arr = [int(num) for num in input().split()]
        s.bobSort(arr[1:])
