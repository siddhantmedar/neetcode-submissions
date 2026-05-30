class Solution:
    def countBits(self, n: int) -> List[int]:
        def util(n):
            cnt = 0
            while n:
                n = n&(n-1)
                cnt+=1

            return cnt

        return [util(ele) for ele in range(n+1)]