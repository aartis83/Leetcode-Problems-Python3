class Solution:
    def eraseOverlapIntervals(self, intervals):

        if not intervals:
            return 0

        erase_count = 0

        intervals.sort(key=lambda interval: interval[0])

        previous_end = intervals[0][1]

        for i in range(1,len(intervals)):
            interval = intervals[i]
            start = interval[0]
            end = interval[1]

            if start < previous_end:
                erase_count += 1
                previous_end = min(previous_end, end)

            else:
                previous_end = end

        return erase_count