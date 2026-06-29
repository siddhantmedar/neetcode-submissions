class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l,r):
            while l<len(s) and r>=0 and l<=r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False

            return True

        start,end = 0,len(s)-1

        while start<len(s) and end>=0 and start<=end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                return is_palindrome(start+1,end) or is_palindrome(start,end-1)

        return True