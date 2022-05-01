"""
书本分发
Description

You are given N number of books. Every ith book has Pi number of pages. You have to allocate books to M number of students. There can be many ways or permutations to do so. In each permutation one of the M students will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is minimum of those in all the other permutations, and print this minimum value. Each book will be allocated to exactly one student. Each student has to be allocated at least one book.每一个学生只能分配连续出现的书本。


Input

The first line contains 'T' denoting the number of testcases. Then follows description of T testcases:Each case begins with a single positive integer N denoting the number of books.The second line contains N space separated positive integers denoting the pages of each book.And the third line contains another integer M, denoting the number of studentsConstraints:1<= T <=70，1<= N <=50，1<= A [ i ] <=250，1<= M <=50，Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see explanation for better understanding)


Output


"""


class Solution:
    def solute(self, n: int, arr: list, m: int):
        dp = []
        for i in range(m):
            dp.append([])
            for j in range(n):
                dp[i].append(-1)
        dp[0][0] = arr[0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + arr[j]
        for i in range(1, m):
            for j in range(i, n):
                dp[i][j] = min([max(dp[i-1][x], sum(arr[x+1:j+1])) for x in range(i-1, j)])
        print(dp[m-1][n-1])


if __name__ == "__main__":
    s = Solution()
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(p) for p in input().split()]
        m = int(input())
        s.solute(n, arr, m)
