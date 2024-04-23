class Solution:
    def isValid(self, s: str) -> bool:
        fechadores = [")", "}", "]"]
        dicdelimitadores = { ")": "(", "}":"{", "]": "["}
        ds = list(s)
                
        while len(ds) > 0:
            toPop = 9999999
            for i in range(len(ds)):
                if ds[i] in fechadores:
                    if ds[i-1] == dicdelimitadores[ds[i]]:
                        if ds[i-1] == ds[-1]:
                            break
                        toPop = i-1
            if toPop == 9999999:
                return False
            
            ds.pop(toPop+1)
            ds.pop(toPop)
                
        return True