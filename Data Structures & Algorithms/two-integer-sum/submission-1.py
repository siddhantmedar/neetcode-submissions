class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mp = dict()

        for i in range(n):
            complement = target-nums[i] # nums[j]
            if complement in mp:
                return [mp[complement],i]
            
            mp[nums[i]] = i

        return []


#  2 2 3 4 target = 6