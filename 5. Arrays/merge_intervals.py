def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sorting the intervals
        intervals.sort(key = lambda x : x[0])
        output = [intervals[0]]

        for start,end in intervals[1:]:
            last_element = output[-1][1]
            if start <= last_element:
                output[-1][1] = max(end,last_element)
            else:
                output.append([start,end])
        return output
