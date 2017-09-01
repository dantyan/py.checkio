import collections


def _counts(data):
    # Generate a table of sorted (value, frequency) pairs.
    table = collections.Counter(iter(data)).most_common()
    if not table:
        return table
    # Extract the values with the highest frequency.
    maxfreq = table[0][1]
    for i in range(1, len(table)):
        if table[i][1] != maxfreq:
            table = table[:i]
            break
    return table


def checkio(s: str):
    a = [z for z in iter(s.lower()) if z.isalpha()]

    table = _counts(a)
    if len(table) == 1:
        return table[0][0]
    else:
        return sorted(table)[0][0]


if __name__ == '__main__':
    assert checkio("Hello World!") == "l"
    assert checkio("How do you do?") == "o"
    assert checkio("One") == "e"
    assert checkio("Oops!") == "o"
    assert checkio("AAaooo!!!!") == "a"
    assert checkio("abe") == "a"
