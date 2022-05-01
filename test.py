class Solution:
    def dfs(self,requests: list[list[int]], index: int):
        if index == len(self.building):
            if self.zero_count == len(self.building):
                self.max_count = max(self.max_satisfy, self.satisfy)
        self.dfs(requests, index + 1)
        out_index = requests[index][0]
        in_index = requests[index][1]
        tmp_zero_count = self.zero_count
        self.building[out_index] -= 1
        self.zero_count -= 0 if self.building[out_index] == 0 else 1
        self.building[out_index] += 1
        self.zero_count -= 0 if self.building[in_index] == 0 else 1
        self.satisfy += 1
        self.dfs(requests, index + 1)
        self.satisfy -= 1
        self.building[out_index] -= 1
        self.building[in_index] += 1
        self.zero_count = tmp_zero_count

    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        self.max_satisfy = 0
        self.satisfy = 0
        self.building = [0]*n
        self.zero_count = n
        self.dfs(requests, 0)
        return self.max_satisfy

