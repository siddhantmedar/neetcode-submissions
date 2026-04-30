class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for ele in nums:
            if count==0:
                candidate = ele
            count +=1 if ele==candidate else -1
        
        return candidate