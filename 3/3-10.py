"""
对称子字符串
"""
class Solution:
    def solute(self, l):
        if len(l) <= 1:
            return 0
        else:
            res = 0
            for i in range(1, len(l)):
                step = 1
                while i - step >= 0 and i + step - 1 < len(l):
                    if sum(l[i-step:i]) == sum(l[i:i+step]) and step > res:
                        res = step
                    step += 1
            return res * 2

if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        l = list(map(int, input()))
        result = s.solute(l)
        print(result)