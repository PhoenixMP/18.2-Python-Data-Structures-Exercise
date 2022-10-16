def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    string = ''
    phrase_list = list(phrase)
    phrase_list.reverse()
    return string.join(phrase_list)


print(reverse_string('awesome'))
print(reverse_string('sauce'))
