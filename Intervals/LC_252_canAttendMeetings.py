# Given an array of meeting time intervals consisting of start and end
# times [s1, e1], [s2, e2], ... , determine if a person could attend
#  all meetings.
# ---------------------------
# canAttendMeetings([[0, 30], [5, 10], [15, 20]]) --> False
# canAttendMeetings([[2, 4], [7, 10]]) --> True


class Solution:
    def canAttendMeetings(self, intervals):

        start = []
        end = []

        for sub_list in intervals:
            start.append(sub_list[0])
            end.append(sub_list[1])

            start.sort()
            end.sort()

        for i in range(len(intervals) - 1):
            if start[i + 1] < end[i]:
                return False

        return True
