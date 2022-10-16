def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    s_vowels = []
    vowel_index = set()
    vowels = set("aioue")
    s_list = list()
    for i, char in enumerate(s):
        if char in vowels:
            s_vowels.append(char)
            vowel_index.add(i)
    count = -1
    for i, char in enumerate(s):

        if i in vowel_index:
            count += 1
            s_list.append(s_vowels[::-1][count])
        else:
            s_list.append(char)
    return "".join(s_list)


print(reverse_vowels("Hello!"))


print(reverse_vowels("Tomatoes"))


print(reverse_vowels("Reverse Vowels In A String"))


print(reverse_vowels("aeiou"))


print(reverse_vowels("why try, shy fly?"))
