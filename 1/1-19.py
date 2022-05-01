"""
快排
"""
class Solution:
    def quickSort(self, arr: list, start: int, end: int):
        if start >= end:
            return
        num = arr[start]
        index_left = start
        index_right = end
        while index_right > index_left:
            while arr[index_right] > num and index_right > index_left:
                index_right -= 1
            while arr[index_left] <= num and index_right > index_left:
                index_left += 1
            tmp = arr[index_right]
            arr[index_right] = arr[index_left]
            arr[index_left] = tmp
        arr[start] = arr[index_left]
        arr[index_left] = num
        self.quickSort(arr, start, index_left - 1)
        self.quickSort(arr, index_left + 1, end)
        return



if __name__ == "__main__":
    s = Solution()
    arr = [int(num) for num in input().split()]
    arr = arr[1:]
    s.quickSort(arr, 0, len(arr) - 1)
    print(" ".join([str(num) for num in arr]))
