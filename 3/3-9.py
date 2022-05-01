"""
字符串匹配
"""
class Solution:
    def solute(self, txt: str, pat: str):
        idc = []
        begin = 0
        while begin < len(txt):
            idx = txt.find(pat, begin)
            if idx == -1:
                break
            idc.append(idx)
            begin = idx + 1
        return idc

if __name__ == "__main__":
    s = Solution()
    for _ in range(int(input())):
        txt, pat = input().split(',')
        print(' '.join(map(str, s.solute(txt, pat))))