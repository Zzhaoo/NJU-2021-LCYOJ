"""
1. 假设你有一只山羊和一只狼需要在一个有向图中从一个结点s到结点t。
为了避免狼吃掉山羊，它们所走的道路不能有公共边。假定存在这样的
路径，请你描述一个在G中找出两条不相交路径的多项式算法，以帮助
狼和羊顺利从s到t。
"""
import heapq


class Solution:
    def __init__(self):
        self.graph_map = {}
        self.path = []

    def solute(self, graph: list[list[int]], source: int, destination: int):
        for i in range(len(graph)):
            self.graph_map[i] = graph[i]
        self.dfs(source, destination)

    def dfs(self, now: int, destination: int):
        self.path.append(now)
        if now == destination:

            return
        for node in self.graph_map[now]:
            self.dfs(destination)
        self.path.pop()
        return







if __name__ == "__main__":
    graph = [[],
             [],
             [],
             []]
    s = Solution()
