def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase_set = set(phrase.lower())
    vowel = {char for char in phrase_set if "aeiou".find(char) != -1}
    return {letter: phrase.lower().count(letter) for letter in vowel}


print(vowel_count('rithm school'))
print(vowel_count('HOW ARE YOU? i am great!'))
