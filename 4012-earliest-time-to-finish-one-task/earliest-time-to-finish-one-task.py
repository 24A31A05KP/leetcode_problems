class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(sum(task) for task in tasks)