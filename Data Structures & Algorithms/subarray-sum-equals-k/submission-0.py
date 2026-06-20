class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = dict()
        mp[0]=1

        prefix = 0
        res = 0

        for ele in nums:
            prefix+=ele
            if prefix-k in mp:
                res+=mp[prefix-k]
            
            mp[prefix]=1+mp.get(prefix,0)

        return res
