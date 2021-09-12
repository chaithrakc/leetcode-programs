from typing import List


class SolutionMergeIntervals:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]  # initialize to avoid edge case
        for start, end in intervals[1:]:
            lastend = output[-1][1]
            if lastend >= start:
                output[-1][1] = max(lastend, end)  # [1, 5] [2, 4] results in [1, 5] -> take max of the ends
            else:
                output.append([start, end])  # non-overlapping intervals -> just append it to output
        return output

