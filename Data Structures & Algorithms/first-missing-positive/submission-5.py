class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        for i in range(N):
            if nums[i] <= 0:
                nums[i] = N+1

        for i in range(N):
            ele = nums[i]

            idx = abs(ele)-1

            if idx<N and nums[idx]>0:
                nums[idx] = -nums[idx]
        
        for i in range(N):
            if nums[i]>=0:
                return i+1

        return N+1