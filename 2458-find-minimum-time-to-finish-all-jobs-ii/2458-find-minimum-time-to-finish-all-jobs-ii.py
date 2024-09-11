class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs = sorted(jobs)
        workers = sorted(workers)
        d = 1
        for (i,j) in zip(jobs, workers):
            d = max(d, ceil(i/j))
        return d
        