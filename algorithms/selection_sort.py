# Runtime: O(n^2)
def SelectionSort(itemList):
    output = []

    while len(itemList) > 0:
        min_item = min(itemList)
        output.append(min_item)
        itemList.remove(min_item)

    return output


if __name__ == "__main__":
    print(SelectionSort([1, 3, 7, 10, 5, 8, 6, 7]))
    print(SelectionSort([6, 2, 4, 1, 3, 7, 5, 8]))
    print(SelectionSort([0]))
    print(SelectionSort([1, 0]))
