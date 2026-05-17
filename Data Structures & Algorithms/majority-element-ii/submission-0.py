class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp = Counter(nums)

        result = []

        for k,v in mp.items():
            if v > len(nums)//3:    
                result.append(k)

        return result