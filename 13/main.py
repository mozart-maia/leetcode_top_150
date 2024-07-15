class Solution:

    def romanToInt(self, s: str) -> int:
        count = 0
        i = 0
        size = len(s)
        while i < size:
            char = s[i]
            if char == "I":
                if (i+1 < size) and s[i+1] == "V":
                    i += 1
                    count += 4
                elif (i+1 < size) and s[i+1] == "X":
                    i += 1
                    count += 9
                else:
                    count += 1
            if char == "X":
                if (i+1 < size) and s[i+1] == "L":
                    i += 1
                    count += 40
                elif (i+1 < size) and s[i+1] == "C":
                    i += 1
                    count += 90
                else:
                    count += 10
            if char == "C":
                if (i+1 < size) and s[i+1] == "D":
                    i += 1
                    count += 400
                elif (i+1 < size) and s[i+1] == "M":
                    i += 1
                    count += 900
                else:
                    count += 100
            if char == "V":
                count += 5
            if char == "L":
                count += 50
            if char == "D":
                count += 500
            if char == "M":
                count += 1000
            i += 1
            

        return count