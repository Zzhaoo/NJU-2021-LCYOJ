"""
merge sort
"""

class Solution:
    def merge(self, arr: list, start: int, mid: int, end: int):
        tmp = []
        index1 = start
        index2 = mid + 1
        while index1 <= mid and index2 <= end:
            if arr[index1] <= arr[index2]:
                tmp.append(arr[index1])
                index1 +=1
            else:
                tmp.append(arr[index2])
                index2 += 1
        while index1 <= mid:
            tmp.append(arr[index1])
            index1 += 1
        while index2 <= end:
            tmp.append(arr[index2])
            index2 += 1
        for i in range(start, end+1):
            arr[i] = tmp[i-start]





    def mergeSort(self, arr: list, start: int, end: int):
        if start >= end:
            return
        mid_index = int((start + end)/2)
        self.mergeSort(arr, start, mid_index)
        self.mergeSort(arr, mid_index + 1, end)
        self.merge(arr, start, mid_index, end)

if __name__ == "__main__":
    s = Solution()
    arr = [int(num) for num in input().split()]
    arr = arr[1:]
    s.mergeSort(arr, 0, len(arr) - 1)
    print(" ".join([str(num) for num in arr]))
