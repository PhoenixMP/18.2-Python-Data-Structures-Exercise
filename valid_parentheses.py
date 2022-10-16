from pickle import FALSE


def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if len(parens) % 2 != 0:
        return False
    i = -1

    if parens[:len(parens)//2][0] == ")":
        return False

    for paren in parens[:len(parens)//2]:
        i += 1
        if paren == "(" and parens[-1-i] == "(":
            print("( and ( are mirrored")
            return False

        if paren == ")" and parens[-1-i] == ")":
            return False

    return True


print(valid_parentheses("()"))

print(valid_parentheses("()()"))

print(valid_parentheses("(()())"))

print(valid_parentheses(")()"))


print(valid_parentheses("())"))


print(valid_parentheses("((())"))


print(valid_parentheses(")()("))
