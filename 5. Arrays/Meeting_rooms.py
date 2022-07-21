def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x : x[0])
        n = len(intervals)
        for i in range(n-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
