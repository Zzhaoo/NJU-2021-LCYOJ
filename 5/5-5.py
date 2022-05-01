"""
时间分隔
"""
class Solution:
    def solute(self, times: list):
        times = sorted(times, key=lambda x: x[1])
        leave_of_stops = []
        for time in times:
            stopped = False
            for i in range(len(leave_of_stops)):
                if leave_of_stops[i] <= time[0]:
                    leave_of_stops[i] = time[1]
                    stopped = True
                    break
            if not stopped:
                leave_of_stops.append(time[1])
        return len(leave_of_stops)





if __name__ == "__main__":
    s = Solution()
    for _ in range(int(input())):
        n = int(input())
        arrive_time = [int(time) for time in input().split()]
        leave_time = [int(time) for time in input().split()]
        time = [(arrive_time[i], leave_time[i]) for i in range(n)]
        print(s.solute(time))