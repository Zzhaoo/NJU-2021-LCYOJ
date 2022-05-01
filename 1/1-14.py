"""
Description

合并数组

Given K sorted arrays arranged in a form of a matrix, your task is to merge them. You need to complete mergeKArrays function which takes 2 arguments, an arr[k][k] 2D Matrix containing k sorted arrays and an integer k denoting the no. of sorted arrays. The function should return a pointer to the merged sorted arrays. There are multiple test cases. For each test case, this method will be called individually.


Input

The first line of input will denote the no of Test cases then T test cases will follow . Each test cases will contain an integer N denoting the no of sorted arrays. Then in the next line contains all the elements of the array separated by space.（1<=T<=50；1<=N<=10）


Output

The output will be the sorted merged array.



"""
import sys


class Solution:
    def solute(self, k: int, matrix: list):
        index_list = [0 for i in range(k)]
        result = []
        while True:
            has_remain = False
            tmp_min = sys.maxsize
            tmp_min_k = -1
            for i in range(k):
                if index_list[i] < len(matrix[i]):
                    has_remain = True
                    if matrix[i][index_list[i]] <= tmp_min:
                        tmp_min = matrix[i][index_list[i]]
                        tmp_min_k = i
            if not has_remain:
                break
            result.append(tmp_min)
            index_list[tmp_min_k] += 1
        print(" ".join(map(str, result)))



if __name__ == "__main__":
    s = Solution()
    n = int(input())
    for i in range(n):
        k = int(input())
        a = [int(num) for num in input().split()]

        matrix = []
        for j in range(k):
            matrix.append(a[0 + j*k: k + j*k])
        s.solute(k, matrix)

