class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        mp = Counter(s)

        odd_count = 0

        for k,v in mp.items():
            if v%2:
                odd_count+=1

        return odd_count<=1