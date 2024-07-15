class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) > len(haystack):
            return -1
           
        sizen = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                hc = i
                nc = 0
                index = i
                while haystack[hc] == needle[nc]:
                    
                    
                    hc += 1
                    nc += 1
                    if nc >= sizen or hc >= len(haystack):
                        break

                if nc == sizen:
                    return index

        return -1
