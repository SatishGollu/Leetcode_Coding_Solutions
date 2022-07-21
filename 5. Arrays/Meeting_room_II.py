int = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        start_time = sorted([x[0] for x in intervals])
        end_time = sorted([x[1] for x in intervals])
        max_count = 0
        count = 0
        start,end = 0,0
        while start < len(intervals):
            if start_time[start] < end_time[end]:

                start += 1
                count += 1
            else:
                end += 1
                count -= 1
            max_count = max(max_count,count)
        return max_count
