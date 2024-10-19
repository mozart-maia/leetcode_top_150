class Solution:

    def invert(self,bits: str):
        result = ""
        for e in bits:
            if e == "0":
                result = result + "1"
            else:
                result = result + "0"
        return result

    def make_sequence(self,n: int) -> str:
        if n == 1:
            return "0"

        return self.make_sequence(n-1) + "1" + self.invert(self.make_sequence(n-1))[::-1]


    def findKthBit(self, n: int, k: int) -> str:
        sequence = self.make_sequence(n)
        return sequence[k-1]