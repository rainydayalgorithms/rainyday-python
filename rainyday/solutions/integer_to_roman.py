def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """

    # INTEGER TO ROMAN
    # You are given an integer. Return its value in Roman numerals

    integer_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_values = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    converted_value = ""

    for i in range (0, len(integer_values)):
        while num >= integer_values[i]:
            converted_value += roman_values[i]
            num -= integer_values[i]

    return converted_value
