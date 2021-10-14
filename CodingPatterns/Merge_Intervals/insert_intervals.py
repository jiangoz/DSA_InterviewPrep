# Given a list of non-overlapping intervals sorted by their start time,
# insert a given interval at the correct position and merge all necessary intervals
# to produce a list that has only mutually exclusive intervals.

def insert(intervals, new_interval):
    merged = []
    # TODO: Write your code here
    # insert new interval to its correct location
    sorted_intervals = insert_helper(intervals, new_interval)
    # add first interval to merged list
    merged.append(sorted_intervals[0])
    # go through the list of intervals and merge overlapping ones
    for x in sorted_intervals[1:]:
        # assume current is x and i is most recent interval in merged
        # possible overlap scenarios:
        """
        iiiiii      iiiiii    iiiiii 
        xxx           xxxx      xxx

        iiiiii      iiiiii    iiiiii
          xxxxxxx   xxxxxx         x

        """
        most_recent = merged[-1]

        # there is overlap
        if x[0] <= most_recent[1]:
            # make the biggest possible "merged" interval
            m = [most_recent[0], max(x[1], most_recent[1])]
            # remove recent interval to make room
            merged.pop()
            merged.append(m)
        else:
            # no overlap; just append
            merged.append(x)

    return merged

# helper method to insert the new interval at its correct location


def insert_helper(intervals, new_interval):
    # check both ends
    if new_interval[0] < intervals[0][0]:
        intervals.insert(0, new_interval)
        return intervals
    elif new_interval[0] > intervals[-1][0]:
        intervals.append(new_interval)
        return intervals

    for i in range(len(intervals)-1):
        # compare the start of new_interval with "neighbors"
        if (new_interval[0] >= intervals[i][0]
                and new_interval[0] <= intervals[i+1][0]):
            # insert the new interval in between
            intervals.insert(i+1, new_interval)
            break

    return intervals

# official solution: different way


def insert2(intervals, new_interval):
    merged = []
    i, start, end = 0, 0, 1

    # skip (and add to output) all intervals that come before the 'new_interval'
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    # merge all intervals that overlap with 'new_interval'
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1

    # insert the new_interval
    merged.append(new_interval)

    # add all the remaining intervals to the output
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


def main():
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " +
          str(insert([[2, 3], [5, 7]], [1, 4])))


main()
