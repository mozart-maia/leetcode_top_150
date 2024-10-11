def clearing_and_convert_to_list(text):
    text = text.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz1234567890"
    return [x for x in text if x in alpha]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            True
        list_chars = clearing_and_convert_to_list(s)
        start = 0
        end = len(list_chars) - 1
        indexs = 0
        indexe = 0
        is_palindrome = True
        while True:
            if start >= end:
                break
            if list_chars[start] != list_chars[end]:
                is_palindrome = False
                break
            start += 1
            end -= 1

        return is_palindrome