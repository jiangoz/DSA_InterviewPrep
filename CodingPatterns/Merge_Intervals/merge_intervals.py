# Given a list of intervals, merge all the overlapping intervals
# to produce a list that has only mutually exclusive intervals.

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
    merged = []
    # TODO: Write your code here
    # sort by interval starting point
    intervals.sort(key=(lambda x: x.start))

    # add first interval to merged
    merged.append(intervals[0])

    # iterate through the rest of the intervals
    for i in intervals[1:]:
        # compare the "most recent" interval in merged with i
        recent = merged[-1]

        # no overlap
        if i.start > recent.end:
            merged.append(i)
        # partly overlap
        if i.start <= recent.end and i.end >= recent.end:
            # create a merged interval
            m = Interval(recent.start, i.end)
            # remove recent interval and add m to merged
            merged.pop()
            merged.append(m)
        # complete overlap
        if i.start <= recent.end and i.end < recent.end:
            continue

    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


main()
