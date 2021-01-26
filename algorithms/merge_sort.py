# Runtime: O(nlog(n))
def MergeSort(itemlist):

    # base case
    if (len(itemlist) == 1):
        return itemlist

    m = len(itemlist) // 2
    left = MergeSort(itemlist[:m])  # recursively sort left half
    right = MergeSort(itemlist[m:])  # recursively sort right half

    # helper function, traverse both sublists and compare their elements
    def Merge(leftHalf, rightHalf):
        output = []
        i = 0  # pointer of left sublist
        j = 0  # pointer of right sublist

        # make sure i and j are within sublist bounds
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:  # left element is smaller
                output.append(leftHalf[i])
                i += 1  # take element from left sublist
            elif leftHalf[i] > rightHalf[j]:  # right element is smaller
                output.append(rightHalf[j])
                j += 1  # take element from right sublist
            else:
                # left element = right element
                output.append(leftHalf[i])
                output.append(rightHalf[j])  # take both elements
                i += 1
                j += 1

        # check which sublist still has elements "remaining", and append them (it was sorted already)
        if i >= j:
            output += rightHalf[j:]
        else:
            output += leftHalf[i:]

        return output

    # merge the sorted left sublist and right sublist
    return Merge(left, right)


if __name__ == "__main__":
    print(MergeSort([1, 3, 7, 10, 5, 8, 6, 7]))
    print(MergeSort([6, 2, 4, 1, 3, 7, 5, 8]))
    print(MergeSort([0]))
    print(MergeSort([1, 0]))
