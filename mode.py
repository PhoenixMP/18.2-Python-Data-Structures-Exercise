def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    last_val = 0
    count = -1

    for val in list(counter.values()):
        count += 1
        print(f'count is {count}')
        if val > last_val:
            last_val = val
            val_index = count
            print(f'index is {val_index}')
        print(f'index is {val_index}')
    return (list(counter.keys())[val_index])

    # return list(counter.keys())[val_index]


print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))
