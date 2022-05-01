"""
拓扑排序解的个数
"""
import collections

class Solution:
    def solute(self, links):
        graph = collections.defaultdict(list)
        starts = set()
        follow = set()
        for edge in links:
            graph[edge[0]].append(edge[1])
            starts.add(edge[0])
            follow.add(edge[1])
        starts -= follow
        def dfs(node):
            if not graph[node]:
                return 1
            ans = 0
            for nx in graph[node]:
                ans += dfs(nx)
            return ans
        return sum(dfs(node) for node in starts)

if __name__ == "__main__":
    s = Solution()
    for _ in range(int(input())):
        links = [pair.split() for pair in input().split(',')]
        del links[0][0]
        print(s.solute(links))