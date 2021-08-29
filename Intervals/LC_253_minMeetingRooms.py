# Given an array of meeting time intervals consisting of start and end
# times [[s1,e1], [s2,e2],...], find the minimum number of conference
# rooms required.

# Example1
#     Input: intervals = [(0,30),(5,10),(15,20)]
#     Output: 2
#     Explanation:
#     We need two meeting rooms
#     room1: (0,30)
#     room2: (5,10),(15,20)

# Example2
#     Input: intervals = [(2,7)]
#     Output: 1
#     Explanation:
#     Only need one meeting room


class Solution:
    def minMeetingRooms(self, intervals):

        if not intervals:
            return 0

        priority_queue = []

        from heapq import heappush, heappop

        intervals.sort(key=lambda interval: interval.start)
        heappush(priority_queue, intervals[0].end)

        for i in range(1, len(intervals)):
            curr_interval = intervals[i]
            earliest_end = priority_queue[0]

            if curr_interval.start >= earliest_end:
                heappush(priority_queue, curr_interval.end)
                heappop(priority_queue)
            else:
                heappush(priority_queue, curr_interval.end)

        return len(priority_queue)




