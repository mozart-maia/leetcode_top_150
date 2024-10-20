class Solution:
    def intToRoman(self, num: int) -> str:
        numerals_romans = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        roman = ""
        for e in numerals_romans:
            value = e[0]
            symbol = e[1]
            while num >= value:
                roman = roman + symbol
                num -= value
        return roman
