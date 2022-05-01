"""
交换数使得两个数组和相差最小
"""
import itertools


class Solution:
    def solute(self, A, B):
        A.extend(B)
        size = len(A)
        h = int(size / 2)
        sum1 = 0
        qs = list(itertools.combinations(A, h))
        for h in range(len(A)):
            sum1 += int(A[h])
        st = len(qs)
        D = []
        ans = 999999999
        for i in range(st):
            D.extend(qs[i])
            sum = 0
            for j in range(len(D)):
                sum += int(D[j])
            gd = sum1 - sum
            sg = abs(sum - gd)
            if (ans > sg):
                ans = sg
        return ans


if __name__ == "__main__":
    s = Solution()
    for _ in range(int(input())):
        a = [int(num) for num in input().split()]
        b = [int(num) for num in input().split()]
        print(s.solute(a, b))
