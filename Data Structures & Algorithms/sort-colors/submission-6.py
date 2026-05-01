class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        low = mid = 0
        high = n-1

        while mid <= high:
            if nums[high]==2:
                high-=1
            
            elif low==mid and nums[low]==0:
                low+=1
                mid+=1
            
            elif nums[mid]==2 and nums[mid]>nums[high]:
                nums[mid],nums[high] = nums[high],nums[mid]
            
            elif nums[low] > nums[mid]:
                nums[low],nums[mid] = nums[mid],nums[low]
                low+=1
            
            else:
                mid+=1
        
        return nums
