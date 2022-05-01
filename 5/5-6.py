"""
管道网络
"""
class Solution:
    def solute(self, pairs: list):
        link, vals = {}, {}
        for pair in pairs:
            link[pair[0]] = pair[1]
            vals[(pair[0], pair[1])] = pair[2]
        starts = set(link.keys()) - set(link.values())
        ans = []
        for s in starts:
            e = link[s]
            val = vals[(s, e)]
            while e in link:
                val = min(val, vals[e, link[e]])
                e = link[e]
            ans.append((s, e, val))
        return sorted(ans)

if __name__ == "__main__":
    s = Solution
    for _ in range(int(input())):
        p, t = map(int, input().strip().split())
        pairs = [tuple(map(int, input().strip().split())) for _ in range(t)]
        res = s.solute(p, pairs)
        print(len(res))
        for ans in res:
            print(*ans)