"""
Searching_4
"""
class Solution:
    def zeroPoint(self, arr, n):
        ans = []
        for i in range(n - 1):
            tmp = 0
            tmpL = arr[i]
            tmpR = arr[i + 1]
            while True:
                left, right = 0, 0
                tmp = (tmpL + tmpR) / 2
                for l in range(i + 1):
                    left += 1.0 / (tmp - arr[l])
                for r in range(i + 1, n):
                    right += 1.0 / (arr[r] - tmp)
                if left - right > 0.000000001:
                    tmpL = tmp
                elif right - left > 0.000000001:
                    tmpR = tmp
                else:
                    break
            ans.append(tmp)
        ans = list(map(lambda x: round(x, 2), ans))
        ans = map(lambda x: '%.02f' % x, ans)
        return ans


if __name__ == "__main__":
    s = Solution()
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(float, input().split()))
        ans = s.zeroPoint(arr, n)
        print(' '.join(ans))