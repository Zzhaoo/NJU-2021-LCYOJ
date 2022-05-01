"""
插入排序
"""
class Solution:
    def insertSort(self, arr: list):
        for i in range(len(arr)):
            tmp = arr[i]
            index = i
            for j in range(0, i):
                if tmp < arr[j]:
                    for m in range(i-1, j-1, -1):
                        arr[m+1] = arr[m]
                    index = j
                    break
            arr[index] = tmp
        print(" ".join([str(num) for num in arr]))




if __name__ == "__main__":
    s = Solution()
    n = int(input())
    for _ in range(n):
        arr = [int(num) for num in input().split()]
        s.insertSort(arr[1:])
