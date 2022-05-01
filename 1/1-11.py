"""
Description

You are provided with marks of N students. A student's Marks in Physics, Chemistry and Maths are provided to you. You want to sort the Student's Numbers in ASCENDING Order of their Physics Marks. Now, Once this is done, Only those students who have Same Marks in Physics have to be sorted in theDESCENDING order of their Chemistry Marks. And now finally, Once this is done too. You need to Sort all those Students who have Same Marks in Physics and Chemistry in ASCENDING ORDER Of their Maths marks.


Input

The First line contains an integer T, the number of testcases.The first line of each testcase contains an integer N , the total number of students. The Next N lines each contains 3 integers P,C,M containing the Physics, Chemistry and Maths' marks of ith student.（1<=T<=10；1<= N <=10000；1<=Pi,Ci,Mi<=1000）


Output

Print the Required Sorted Array of Marks.（Note: While swapping two student's data(while sorting), you need to swap all the P,C,M marks of the students. That is You need to swap the whole tuple in a swap and not just the marks of any 1 subject.）



"""

def larger(mark1: list, mark2: list):
    if mark1[0] > mark2[0]:
        return True
    elif mark1[0] == mark2[0]:
        if mark1[1] < mark2[1]:
            return True
        elif mark1[1] == mark2[1]:
            if mark1[2] > mark2[2]:
                return True
    return False
def swap(marks: list, index_right: int, index_left: int):
    tmp = marks[index_right]
    marks[index_right] = marks[index_left]
    marks[index_left] = tmp

def quick_sort(marks: list, start_index: int, end_index: int):
    if start_index >= end_index:
        return
    middle = marks[start_index]
    index_left = start_index
    index_right = end_index
    while (index_left != index_right):
        while (index_right > index_left and larger(marks[index_right], middle)):
            index_right -= 1
        while (index_left < index_right and not larger(marks[index_left], middle)):
            index_left += 1
        swap(marks, index_right, index_left)
    swap(marks, start_index, index_left)
    quick_sort(marks, start_index, index_left - 1)
    quick_sort(marks, index_left + 1, end_index)


class Solution:
    def solute(self, marks: list):
        quick_sort(marks, 0, len(marks)-1)
        for mark in marks:
            print("{} {} {}".format(mark[0], mark[1], mark[2]))




if __name__ == "__main__":
    s = Solution()
    n = int(input())
    for i in range(n):
        m = int(input())
        marks = []
        for j in range(m):
            marks.append([int(mark) for mark in input().split()])
        s.solute(marks)

