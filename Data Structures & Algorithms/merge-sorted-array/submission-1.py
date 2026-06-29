class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            i,j = 0,0

            while i<len(nums1) and j<len(nums2):
                nums1[i] = nums2[j]
                i+=1
                j+=1
            return
        
        if n==0:
            return
        
        def make_space(nums,idx,curr_loc):
            while idx-1>=curr_loc:
                nums[idx] = nums[idx-1]
                idx-=1

        curr_idx = m

        i,j = 0,0

        while i<len(nums1) and j<len(nums2):
            if nums1[i] > nums2[j]:
                make_space(nums1,curr_idx,i)
                
                curr_idx+=1
                
                nums1[i] = nums2[j]
                j+=1

                if curr_idx >= len(nums1):
                    break
            
            i+=1

        while curr_idx<len(nums1) and j<len(nums2):
            nums1[curr_idx] = nums2[j]
            curr_idx+=1
            j+=1
        return

# 10 20 30 40 50 | 15 35
#                        _

# 10 15 20 30 35 40 50
#                _
#                       _



