"""
最小交换次数
"""

class Solution:
    def solute(self, arr: list):
        exchange_num = 0
        arr_sorted = sorted(arr)
        index_map = {}
        for i in range(len(arr_sorted)):
            index_map[arr_sorted[i]] = i
        for i in range(len(arr)):
            while i != index_map[arr[i]]:
                tmp = arr[index_map[arr[i]]]
                arr[index_map[arr[i]]] = arr[i]
                arr[i] = tmp
                exchange_num += 1
        print(exchange_num)


if __name__ == "__main__":
    s = Solution()
    n = int(input())
    for _ in range(n):
        m = int(input())
        arr = [int(num) for num in input().split()]
        s.solute(arr)
