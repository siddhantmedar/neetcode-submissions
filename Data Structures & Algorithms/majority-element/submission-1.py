class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for ele in nums:
            if candidate is None:
                candidate = ele
                count = 1
            elif candidate==ele:
                count+=1
            else:
                count-=1
                if count==0:
                    candidate = ele
                    count = 1

        return candidate