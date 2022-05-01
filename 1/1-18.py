"""
计数排序
"""


class Solution:
    def countSort(self, arr: list):
        if len(arr) < 1:
            print(" ".join([str(num) for num in arr]))
            return
        max_num = max(arr)
        min_num = min(arr)
        count = [0]*(max_num - min_num + 1)
        for num in arr:
            count[num - min_num] += 1
        arr.clear()
        for i in range(len(count)):
            for _ in range(count[i]):
                arr.append(i + min_num)
        print(" ".join([str(num) for num in arr]))


if __name__ == "__main__":
    s = Solution()
    n = int(input())
    for _ in range(n):
        arr = [int(num) for num in input().split()]
        s.countSort(arr[1:])
