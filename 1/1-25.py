"""
按照数值个数排序
"""
import functools
import collections
def mycmp(tuple1: tuple, tuple2: tuple):
    if tuple1[1] > tuple2[1]:
        return -1
    elif tuple1[1] < tuple2[1]:
        return 1
    else:
        if tuple1[0] > tuple2[0]:
            return 1
        elif tuple1[0] < tuple2[0]:
            return -1
        else:
            return 0
class Solution:

    def solute(self, nums):
        count = collections.Counter(nums)
        res = []
        for val, c in sorted(count.items(), key=functools.cmp_to_key(mycmp)):
            res += [val] * c
        return res

if __name__ == "__main__":
    s = Solution()
    for _ in range(int(input())):
        input()
        nums = list(map(int, input().split()))
        print(*s.solute(nums))
