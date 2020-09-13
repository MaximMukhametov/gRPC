from typing import List


def maximum_product_of_tree_numbers(array: List[float]) -> float:
    """
    This function calculates the maximum
    product of three numbers in an array.
    The algorithm works with time complexity O(n).
    """
    if len(array) < 3:
        raise ValueError('The array must contain at least 3 elements')

    min1 = max(array)
    min2 = max(array)
    max1 = min(array)
    max2 = min(array)
    max3 = min(array)

    for item in array:
        if item <= min1:
            min2 = min1
            min1 = item
        elif item <= min2:
            min2 = item

        if item >= max1:
            max3 = max2
            max2 = max1
            max1 = item
        elif item >= max2:
            max3 = max2
            max2 = item
        elif item >= max3:
            max3 = item

    return max(min1 * min2 * max1, max1 * max2 * max3)
