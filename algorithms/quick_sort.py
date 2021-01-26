# Runtime: O(nlog(n)) - divide n' conquer
# Theoretically worst is O(n^2)
def QuickSort(itemList):

    # base case
    if len(itemList) <= 1:
        return itemList

    lower = []
    higher = []
    pivot = itemList.pop()

    for i in itemList:
        if i > pivot:
            higher.append(i)
        else:
            lower.append(i)

    return QuickSort(lower) + [pivot] + QuickSort(higher)


if __name__ == "__main__":
    print(QuickSort([1, 3, 7, 10, 5, 8, 6, 7]))
    print(QuickSort([6, 2, 4, 1, 3, 7, 5, 8]))
    print(QuickSort([0]))
    print(QuickSort([1, 0]))
