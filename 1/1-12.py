"""
未满分

Description

Consider a big party where a log register for guest’s entry and exit times is maintained. Find the time at which there are maximum guests in the party. Note that entries in register are not in any order.


Input

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the entry and exit array. Then the next two line contains the entry and exit array respectively.(1<=T<=10^5;1<=N<=10^5;1<=entry[i],exit[i]<=10^5)


Output

Print the maximum no of guests and the time at which there are maximum guests in the party.
"""
class Solution:
    # TODO
    def solute(self, enters: list, exits: list):
        list.sort(enters)
        list.sort(exits)
        enter_index, exit_index, count = 0, 0, 0
        max_count, max_time = 0, 0
        while enter_index < len(enters):
            if enters[enter_index] <= exits[exit_index]:
                count += 1
                if count > max_count:
                    max_count, max_time = count, enters[enter_index]
                enter_index += 1
            elif enters[enter_index] > exits[exit_index]:
                count -= 1
                exit_index += 1
        print(max_count, max_time)


if __name__ == "__main__":
    s = Solution()
    n = int(input())
    for i in range(n):
        size = int(input())
        enters = [int(time) for time in input().split()]
        exits = [int(time) for time in input().split()]
        s.solute(enters, exits)
