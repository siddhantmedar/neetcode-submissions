class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s,ignore_idx=None):
            l,r = 0,len(s)-1

            while l<len(s) and r>=0 and l<=r:
                if l==ignore_idx:
                    l+=1
                    continue
                if r==ignore_idx:
                    r-=1
                    continue
                
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False

            return True
    
        for i in range(len(s)):
            if is_palindrome(s,i):
                return True

        return False