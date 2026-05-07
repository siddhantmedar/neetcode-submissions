class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1]*n
        right = [1]*n
        result = [None]*n

        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]

        for i in range(n-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
            result[i] = left[i]*right[i]
        
        result[n-1] = left[n-1]*right[n-1]

        return result

        # 1  2   4   6
        # 1  1   2   8 
        # 48 24  6   1 reversed