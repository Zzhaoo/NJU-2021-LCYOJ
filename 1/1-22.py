"""
shell sort
"""

class Solution:
    def shell(self, arr: list, gaps: list):
        """shell排序其实就是分组进行插入排序"""
        for k in range(len(gaps)):
            interval = gaps[k]
            for i in range(interval, len(arr)):
                tmp = arr[i]
                j = i
                while j - interval >= 0 and arr[j - interval] > tmp:
                    arr[j] = arr[j - interval]
                    j -= interval
                arr[j] = tmp



if __name__ == "__main__":
    s = Solution()
    n = int(input())
    for i in range(n):
        arr = [int(num) for num in input().split()]
        gaps = [int(num) for num in input().split()]
        s.shell(arr, gaps)
        print(" ".join([str(num) for num in arr]))
