# Question 13: Balanced Symbols
# Check if the brackets in a string are balanced.
#
# Input: "{[()]}"
# Output: True
#
# Input: "{[(])}"
# Output: False


def has_balanced_symbols(text):
    if not isinstance(text, str):
        return False

    stack = []

    matching_symbols = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in text:
        if character in "([{":
            stack.append(character)

        elif character in matching_symbols:
            if not stack or stack.pop() != matching_symbols[character]:
                return False

    return len(stack) == 0


def run_tests():
    assert has_balanced_symbols("{[()]}") is True
    assert has_balanced_symbols("{[(])}") is False
    assert has_balanced_symbols("") is True
    assert has_balanced_symbols("((") is False
    assert has_balanced_symbols("]") is False

    assert has_balanced_symbols(
        "function(value) { return [value]; }"
    ) is True

    assert has_balanced_symbols(None) is False
    assert has_balanced_symbols(123) is False

    print("All timed challenge tests passed.")


if __name__ == "__main__":
    run_tests()
