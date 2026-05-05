class Solution:
    def countElements(self, arr: List[int]) -> int:
        bucket = [0]*1001
        
        for ele in arr:
            bucket[ele]+=1

        res = 0
        for i,cnt in enumerate(bucket):
            if i+1<len(bucket) and bucket[i+1] > 0:
                res+=cnt

        return res