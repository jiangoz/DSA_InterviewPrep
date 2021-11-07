# Given an array of intervals representing ‘N’ appointments,
# find out if a person can attend all the appointments.

# Time: O(N * log(N))
# Space: O(N) needed for sorting

def can_attend_all_appointments(intervals):
    # TODO: Write your code here

    # sort by interval start time
    intervals.sort(key=(lambda x: x[0]))

    recent = 0

    for i in intervals[1:]:

        # check if there is overlap
        if i[0] < intervals[recent][1]:
            return False
        else:
            # there is no overlap; proceed to check next intervals
            recent += 1

    return True

# Given a list of appointments, find all the conflicting appointments


def find_conflicts(intervals):
    # sort intervals by start time
    intervals.sort(key=(lambda x: x[0]))

    j = 0

    for i in range(1, len(intervals)):
        # compare i with j (previous interval)
        # check if there is overlap/conflict
        if intervals[i][0] < intervals[j][1]:
            print(f'{intervals[j]} and {intervals[i]} conflict.')
        else:
            # there is no overlap; increment to check next interval
            j += 1


def main():
    # false
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    # true
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    # false
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))
    # true
    print("Can attend all appointments: " +
          str(can_attend_all_appointments([[4, 5], [2, 4], [5, 6]])))

    # [4,5] and [3,6] conflict.
    # [3,6] and [5,7] conflict.
    find_conflicts([[4, 5], [2, 3], [3, 6], [5, 7], [7, 8]])


main()
