class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x[1])
        end_so_far = intervals[0][1]
        removed = 0
        for start, finish in intervals[1:]:
            if start < end_so_far:
                removed += 1
            else:
                end_so_far = finish
        return removed
