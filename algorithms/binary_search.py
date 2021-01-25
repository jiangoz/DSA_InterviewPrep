# Runtime: O(log(n))
def BinarySearch(items, target):

    def helper(items, target, l, r):
        if r >= l:
            mid_index = (r+l) // 2
            m = items[mid_index]
            if m == target:
                print(f"{target} was found at index {mid_index}")
                return
            elif m < target:
                # search right side
                helper(items, target, mid_index+1, r)
            elif m > target:
                # search left side
                helper(items, target, l, mid_index-1)
        else:
            print(f"{target} was not found")
            return

    helper(items, target, 0, len(items)-1)

if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    BinarySearch(arr, 4)
    BinarySearch(arr, 3)
    BinarySearch(arr, 1)
    BinarySearch(arr, 2)
