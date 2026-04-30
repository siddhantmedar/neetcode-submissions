class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_hash(s):
            bucket = [0]*26

            for c in s:
                bucket[ord(c)-ord('a')]+=1
            
            return tuple(bucket)

        
        mp = defaultdict(list)

        for s in strs:
            mp[get_hash(s)].append(s)

        return list(mp.values())

        """
        n = size(strs)
        TC: n*(26+L+26) + n the last n is technically all words in input strs
        SC: for dict O(26+26*# of distinct words meaning anagrams + n.L) where L is the max size of a word say
        """