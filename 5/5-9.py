"""
固定和的元素对
"""
import itertools
if __name__ == "__main__":
    for _ in range(int(input())):

        nums = list(map(int, input().split()))
        m = int(input())

        cnt = 0
        for a, b in itertools.combinations(nums, 2):
            if a + b == m:
                cnt += 1
        print(cnt)