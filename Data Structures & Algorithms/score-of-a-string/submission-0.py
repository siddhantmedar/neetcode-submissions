class Solution:
    def scoreOfString(self, s: str) -> int:
        def get_ascii(c):
            return ord(c)-ord('a')
        
        result = 0

        for i in range(len(s)-1):
            result+= abs(get_ascii(s[i])-get_ascii(s[i+1]))

        return result