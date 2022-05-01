"""
覆盖棋盘
"""

class Solution:
    def solute(self, k: int, coor_1: tuple, coor_2: tuple):
        if coor_1 == coor_2:
            return []
        return self.chess_board((0, 0), coor_1, coor_2, 2**k)

    def chess_board(self, left_top: tuple, coor_1: tuple, coor_2: tuple, size: int):
        if size == 1:
            return None
        size = size // 2
        left_top_table = [(left_top[0], left_top[1]), #左上
                          (left_top[0], left_top[1] + size), #右上
                          (left_top[0] + size, left_top[1]), #左下
                          (left_top[0] + size, left_top[1] + size)] #右下
        coor_tmp_table = [(left_top[0] + size - 1, left_top[1] + size - 1),
                          (left_top[0] + size - 1, left_top[1] + size),
                          (left_top[0] + size, left_top[1] + size - 1),
                          (left_top[0] + size, left_top[1] + size)]
        for i in range(4):
            # 找到了，去掉不该返回的两个值，其他两个返回
            if coor_tmp_table[i][0] == coor_2[0] and coor_tmp_table[i][1] == coor_2[1]:
                for j in range(4):
                    left_top = left_top_table[j]
                    if left_top[0] <= coor_1[0] < left_top[0] + size and left_top[1] <= coor_1[1] < left_top[1] + size:
                        del coor_tmp_table[j]
                        break
                coor_tmp_table.remove(coor_2)
                return coor_tmp_table

        # 没找到，就继续递归
        res = None
        for i in range(4):
            left_top = left_top_table[i]
            if left_top[0] <= coor_1[0] < left_top[0] + size and left_top[1] <= coor_1[1] < left_top[1] + size:
                # 在这个格子里
                res = self.chess_board(left_top, coor_1, coor_2, size)
            else:
                res = self.chess_board(left_top, coor_tmp_table[i], coor_2, size)
            if res is not None:
                return res
        return res



if __name__ == "__main__":
    s = Solution()
    n = int(input())
    for i in range(n):
        k, i_1, j_1 = map(int, input().split())
        i_2, j_2 = map(int, input().split())
        res = s.solute(k, (i_1, j_1), (i_2, j_2))
        for j in range(len(res)):
            print(str(res[j][0]) + " " + str(res[j][1]), end='')
            if j != len(res) - 1:
                print(',', end='')

