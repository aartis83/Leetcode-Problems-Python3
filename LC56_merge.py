class Solution:
    def merge(self, intervals):

        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval[0])
        res = [intervals[0]]

        for interval in intervals:
            prev_interval = res[-1]

            if interval[0] <= prev_interval[1]:
                prev_interval[1] = max(interval[1], prev_interval[1])

            else:
                res.append(interval)

        return res
