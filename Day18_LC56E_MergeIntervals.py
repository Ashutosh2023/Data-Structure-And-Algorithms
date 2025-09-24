def mergeOverlappingIntervals(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) <= 1:
        return intervals
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    x, y = sorted_intervals[0][0], sorted_intervals[0][1]
    result = set()
    for i in range(len(sorted_intervals)):
        if sorted_intervals[i][0] > y:
            result.add((x,y))
            x = sorted_intervals[i][0]
            y = sorted_intervals[i][1]
        else:
            y = max(sorted_intervals[i][1], y)
    result.add((x,y))
    return [list(t) for t in result]

intervals = [[1,5],[2,4]]
print(mergeOverlappingIntervals(intervals))

#optimized very similary yet looks good
def mergeOverlappingIntervalsOptm(intervals: list[list[int]]) -> list[list[int]]:
    if len(intervals) <= 1:
        return intervals
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeOverlappingIntervalsOptm(intervals))