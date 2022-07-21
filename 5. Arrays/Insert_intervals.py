# my o(nlogn) solution
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    #adding newinterval to intervals
    intervals.append(newInterval)
    #sort the intervals
    intervals.sort(key = lambda x : x[0])
    #output list
    output = [intervals[0]]
    #iterate
    for start,end in intervals[1:]:
        last_element = output[-1][1]
        if start <= last_element:
            output[-1][1] = max(last_element,end)
        else:
            output.append([start,end])
    return output
#optimized solution
# -- O(n)
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    output = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            output.append(newInterval)
            return output + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            output.append(intervals[i])
        else:
            newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
    output.append(newInterval)
    return output
