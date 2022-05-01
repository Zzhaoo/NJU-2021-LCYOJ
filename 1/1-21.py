"""
倒置个数
"""

class Solution:
    def __init__(self):
        self.count = 0

    def reverseOrdCountHelp(self, arr: list, start: int, mid: int, end: int):
        tmp = []
        index1 = start
        index2 = mid + 1
        while index1 <= mid and index2 <= end:
            if arr[index1] <= arr[index2]:
                tmp.append(arr[index1])
                index1 += 1
            else:
                tmp.append(arr[index2])
                index2 += 1
                self.count += (mid - index1 + 1)
        while index1 <= mid:
            tmp.append(arr[index1])
            index1 += 1
        while index2 <= end:
            tmp.append(arr[index2])
            index2 += 1
        for i in range(start, end+1):
            arr[i] = tmp[i-start]

    def reverseOrdCount(self, arr: list, start: int, end: int):
        if start >= end:
            return
        mid_index = int((start + end)/2)
        self.reverseOrdCount(arr, start, mid_index)
        self.reverseOrdCount(arr, mid_index + 1, end)
        self.reverseOrdCountHelp(arr, start, mid_index, end)

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        s = Solution()
        m = input()
        arr = [int(num) for num in input().split()]
        s.reverseOrdCount(arr, 0, len(arr) - 1)
        print(s.count)