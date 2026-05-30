class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        st = set(nums)
        
        result = 0
        
        for ele in st:
            if ele-1 in st:
                continue
            
            start = ele
            cnt = 0
            while start in st:
                start+=1
                cnt+=1

            result = max(result,cnt)

        return result
            
        