"""
距离问题
"""

from collections import defaultdict
class Solution:
    def solute(self, dict_x, dict_y, dict_xy):
        x_pair_num = 0
        y_pair_num = 0
        xy_pair_num = 0
        for k, v in dict_x.items():
            x_pair_num += v * (v - 1) // 2
        for k, v in dict_y.items():
            y_pair_num += v * (v - 1) // 2
        for k, v in dict_xy.items():
            xy_pair_num += v * (v - 1) // 2
        return x_pair_num + y_pair_num - xy_pair_num


if __name__ == "__main__":
    n = int(input())
    s = Solution()
    for _ in range(n):
        dict_x = defaultdict(int)  # 初始化一个默认值为0的map
        dict_y = defaultdict(int)
        dict_xy = defaultdict(int)
        point_num = int(input())
        for j in range(point_num):
            p = [int(x) for x in input().strip().split(" ")]
            dict_x[p[0]] += 1
            dict_y[p[1]] += 1
            dict_xy[tuple(p)] += 1
        print(s.solute(dict_x, dict_y, dict_xy))
