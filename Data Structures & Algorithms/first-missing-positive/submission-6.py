class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        i = 0

        while i < N:
            idx = nums[i]-1

            if 0<=idx<N and nums[i]!=nums[idx]:
                nums[i],nums[idx] = nums[idx],nums[i]
            else:i+=1

        for i in range(N):
            if nums[i]!=i+1:
                return i+1

        return N+1