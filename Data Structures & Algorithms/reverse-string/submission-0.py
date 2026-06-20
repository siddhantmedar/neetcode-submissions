class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        i,j = 0, N-1

        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1

        return