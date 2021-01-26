# Runtime: O(n^2)
def InsertionSort(itemList):

    for i in range(1, len(itemList)):

        while i > 0 and (itemList[i-1] > itemList[i]):
            itemList[i], itemList[i-1] = itemList[i-1], itemList[i]
            i -= 1

    return itemList


if __name__ == "__main__":
    print(InsertionSort([1, 3, 7, 10, 5, 8, 6, 7]))
    print(InsertionSort([6, 2, 4, 1, 3, 7, 5, 8]))
    print(InsertionSort([0]))
    print(InsertionSort([1, 0]))
