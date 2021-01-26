# Runtime: O(n^2)
def BubbleSort(itemList):

    output = itemList
    swapExists = True

    while (swapExists):
        swapExists = False
        bubbleStart = 0
        for bubbleEnd in range(1, len(itemList)):
            if output[bubbleEnd] < output[bubbleStart]:
                ogBubbleStart = output[bubbleStart]
                output[bubbleStart] = output[bubbleEnd]
                output[bubbleEnd] = ogBubbleStart
                swapExists = True
            bubbleStart += 1

    return output


if __name__ == "__main__":
    print(BubbleSort([3, 8, 3, 5, 10, 7, 7]))
    print(BubbleSort([3, 8, 7]))
    print(BubbleSort([0]))
    print(BubbleSort([6, 2, 4, 1, 3, 7, 5, 8]))
