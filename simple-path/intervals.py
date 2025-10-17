def start_index(interval: list) -> int:
    """return the first int in the list"""
    return interval[0]


def merge_intervals(intervals: list) -> list:
    """merge all overlapping intervals """

    #sort the list based on the first int in each list
    intervals.sort(key=start_index)
    new_intervals = []
    i = 0

    while i < len(intervals) - 1:
        upper_i = intervals[i][-1]
        lower_i = intervals[i+1][0]

        
        if upper_i >= lower_i:
            first = intervals[i][0]
            last = intervals[i+1][-1]
            new_intervals.append([first, last])

        i += 1
    print(new_intervals)




# expected: [[1,6],[8,10],[15,18]]

# input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
ints = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(ints)