def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    lst1 = [int(char) for char in str(num1)]
    lst2 = [int(char) for char in str(num2)]
    lst1.sort()
    lst2.sort()
    return lst1 == lst2


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
