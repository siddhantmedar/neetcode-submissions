class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp = Counter(nums)

        for k,v in mp.items():
            if v>=len(nums)//2:
                return k