"""
是否能通过考试

questions h p i

if p_remain > p:
    time = min(t_i + solute(n - 1, h - t_i, p - p_i, questions[1:]), solute(n - 1, h, p, question[1:]))
else:
    time = t_i + solute(n - 1, h - t_i, p - p_i, questions[1:])

dp[i][j] = min(questions[i][0] + dp[i-1][j - questions[i][0]], dp[i-1][j])

"""


class Solution:
    def solute(self, n: int, h: int, p: int, questions_time: list, questions_point: list):
        dp = [[h + 1] * p for _ in range(n)]
        for i in range(n):
            for j in range(p):
                if i == 0:
                    if j < questions_point[i]:
                        dp[i][j] = questions_time[i]
                    continue
                t_1 = questions_time[i] + dp[i - 1][j - questions_point[i]]
                t_2 = dp[i - 1][j]
                dp[i][j] = min(t_1, t_2)
        if dp[-1][-1] != h + 1:
            print("YES {}".format(dp[-1][-1]))
        else:
            print("NO")


if __name__ == "__main__":
    s = Solution()
    m = int(input())
    for _ in range(m):
        n, h, p = map(int, input().split())
        questions_time = []
        questions_point = []
        for _ in range(n):
            question = [int(num) for num in input().split()]
            questions_time.append(question[0])
            questions_point.append(question[1])
        s.solute(n, h, p, questions_time, questions_point)
