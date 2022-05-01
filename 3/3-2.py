"""
区间第k最小
"""


if __name__ == "__main__":
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        star, stop = map(int, input().split())
        k = int(input())
        inter = [arr[x] for x in range(star - 1, stop)]  # 截取区间
        inter.sort()  # 排序
        print(inter[k - 1])  # 输出第K个

