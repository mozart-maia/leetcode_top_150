class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        trimmed = s.strip()
        splited = trimmed.split()
        return len(splited[-1])