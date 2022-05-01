class Solution:
    def solute(self, arr1: list, arr2: list):
        index1 = 0
        index2 = 0
        sum1 = 0
        sum2 = 0
        res = 0
        while index1 < len(arr1) and index2 < len(arr2):
            if arr1[index1] < arr2[index2]:
                sum1 += arr1[index1]
                index1 += 1
            elif arr1[index1] > arr2[index2]:
                sum2 += arr2[index2]
                index2 += 1
            else:
                sum1 += arr1[index1]
                sum2 += arr2[index2]
                res += max(sum1, sum2)
                sum1 = 0
                sum2 = 0
                index1 += 1
                index2 += 1
        while index1 < len(arr1):
            sum1 += arr1[index1]
            index1 += 1
        while index2 < len(arr2):
            sum2 += arr2[index2]
            index2 += 1
        res += max(sum1, sum2)
        print(res)


if __name__ == "__main__":
    s = Solution()
    c = int(input())
    for _ in range(c):
        n, m = map(int, input().split())
        arr1 = [int(num) for num in input().split()]
        arr2 = [int(num) for num in input().split()]
        s.solute(arr1, arr2)
