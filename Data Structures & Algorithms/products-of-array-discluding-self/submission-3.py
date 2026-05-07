class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1]*n
        right = 1

        for i in range(1,n):
            left[i] = left[i-1]*nums[i-1]

        for i in range(n-1,-1,-1):
            left[i] = left[i]*right
            right = right*nums[i]

        return left

        # 1  2   4   6
        # 1  1   2   8 
        # 48 24  6   1 reversed

        # result and input
        # 1   2  4  6
        # 1   1  2  8 left
        # 48 24  6  1 right
