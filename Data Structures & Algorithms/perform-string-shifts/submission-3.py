class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        delta = 0

        for direction,steps in shift:
            delta+= steps if direction==0 else -steps

        print(delta)
        delta %= len(s)
        
        if delta==0:
            return s
        
        return s[delta:]+s[:delta]