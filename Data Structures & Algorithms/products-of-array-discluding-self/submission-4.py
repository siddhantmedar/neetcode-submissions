class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        right = 1

        for i in range(1,n):
            result[i] = result[i-1]*nums[i-1]

        for i in range(n-1,-1,-1):
            result[i] = result[i]*right
            right = right*nums[i]

        return result

        # 1  2   4   6
        # 1  1   2   8 
        # 48 24  6   1 reversed

        # result and input
        # 1   2  4  6
        # 1   1  2  8 left
        # 48 24  6  1 right
