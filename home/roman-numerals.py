#!/usr/bin/python

def checkio(num):

    """
        I 1 (unus)
        V 5 (quinque)
        X 10 (decem)
        L 50 (quinquaginta)
        C 100 (centum)
        D 500 (quingenti)
        M 1,000 (mille)
    :param num:
    :return:
    """
    elements = (
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    )

    result = ''
    for roman, n in elements:
        if n <= num:
            result += roman * (num // n)
            num %= n

    return result

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print(checkio(3888))
    # assert checkio(6) == 'VI', '6'
    # assert checkio(76) == 'LXXVI', '76'
    # assert checkio(499) == 'CDXCIX', '499'
    # assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'

# checkio(6) == 'VI'
# checkio(76) == 'LXXVI'
# checkio(13) == 'XIII'
# checkio(44) == 'XLIV'
# checkio(3999) == 'MMMCMXCIX'