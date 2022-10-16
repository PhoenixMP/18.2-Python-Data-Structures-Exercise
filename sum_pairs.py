def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    pairs = []
    index = -1
    for num in nums:
        index += 1
        rest = nums[index+1::]
        if num <= goal:
            next = goal-num
            if rest.count(next) > 0:
                pairs.append(
                    {'pair': (num, next), 'index': rest.index(next)+index+1})

    if pairs != []:
        index = pairs[0]['index']
        for pair in pairs:
            if pair['index'] < index:
                index = pair['index']
        for pair in pairs:
            if pair['index'] == index:
                return pair['pair']
    else:
        return ()


print(sum_pairs([1, 2, 2, 10], 4))
print(sum_pairs([4, 2, 10, 5, 1], 6))
print(sum_pairs([5, 1, 4, 8, 3, 2], 7))
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))
