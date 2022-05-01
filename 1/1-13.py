"""
Description

未全过

和为定值的子数组

Given an array A of size N, find all combination of four elements in the array whose sum is equal to a given value K. For example, if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and K = 23, one of the quadruple is “3 5 7 8” (3 + 5 + 7 + 8 = 23).


Input

The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line of input contains two integers N and K. Then in the next line are N space separated values of the array.（1<=T<=100；1<=N<=100；-1000<=K<=1000；-100<=A[]<=100）


Output

For each test case in a new line print all the quadruples present in the array separated by space which sums up to value of K. Each quadruple is unique which are separated by a delimeter "
"""


class Solution:

    def support(self, array: list, path: list, start: int, remain: int, total: int):
        if remain == 0:
            if total == 0:
                print(" ".join(map(str, path)), "$", end="")
            return
        for i in range(start, len(array)):
            if i > start and array[i] == array[i - 1]:
                continue
            path.append(array[i])
            total -= array[i]
            remain -= 1
            self.support(array, path, i + 1, remain, total)
            remain += 1
            total += array[i]
            del (path[-1])

    def solute(self, array: list, total: int):
        array = sorted(array)
        self.support(array, [], 0, 4, total)


if __name__ == "__main__":
    s = Solution()
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        a = [int(num) for num in input().split()]
        s.solute(a, k)
