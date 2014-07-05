def int_to_roman(i):
    roman_map = zip(
        ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
        , (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1))
    result = []
    for roman, num in roman_map:
        while num <= i:
            i -= num
            result.append(roman)
    return "".join(result)