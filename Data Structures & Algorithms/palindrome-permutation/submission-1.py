class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        bit = 0

        for c in s:
            pos = ord(c)-ord('a')
            bit = bit ^ (1<<pos)

        cnt = 0
        while bit:
            bit = bit & (bit-1)
            cnt+=1

        return cnt<=1