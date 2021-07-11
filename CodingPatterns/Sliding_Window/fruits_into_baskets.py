"""
Given an array of characters where each character represents a fruit tree, you are given two baskets, 
and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but you can’t skip a tree once you have started. 
You will pick one fruit from each tree until you cannot, 
i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.
"""


def fruits_into_baskets(fruits):

    maxfruits = 0
    winStart = 0

    # hashmap for keeping track of 2 baskets (# of fruits in each basket)
    baskets = {}

    # how many fruits in the 2 baskets within our "window"
    winFruits = 0

    for winEnd in range(len(fruits)):

        # check if fruit exists in hashmap
        if fruits[winEnd] in baskets:
            baskets[fruits[winEnd]] += 1
        else:
            baskets[fruits[winEnd]] = 1

        winFruits += 1

        # check if basket length/"limit" is invalid
        while len(baskets) > 2:
            # decrement winFruits, and also,
            winFruits -= 1
            # remove outgoing element from fruit basket
            baskets[fruits[winStart]] -= 1
            # check if that basket is empty now
            if baskets[fruits[winStart]] == 0:
                baskets.pop(fruits[winStart])
            # shrink window size
            winStart += 1

        maxfruits = max(maxfruits, winFruits)

    return maxfruits


if __name__ == "__main__":
    fruits1 = ["a", "b", "c", "c", "d", "f", "f"]
    print(fruits_into_baskets(fruits1))  # should be 3
    fruits2 = ["a", "b", "c", "c", "f", "f", "f"]
    print(fruits_into_baskets(fruits2))  # should be 5
