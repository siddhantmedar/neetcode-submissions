class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0

        for j in range(32):
            if (1<<j) & n:
                cnt+=1
        
        return cnt