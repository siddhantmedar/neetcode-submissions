class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)

        for i in range(N):
            if nums[i] < 0:
                nums[i] = math.inf

        for i in range(N):
            ele = nums[i]
            
            if ele==math.inf:
                continue

            idx = abs(ele)-1

            if 0<=idx<N:
                nums[idx] = -nums[idx] if nums[idx] > 0 else -math.inf

        for i in range(N):
            if nums[i]>=0:
                return i+1

        return N+1