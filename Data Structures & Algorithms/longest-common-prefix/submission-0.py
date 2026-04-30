class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn_size = min([len(s) for s in strs])
        prefix = ""

        for i in range(mn_size):
            ch = {s[i] for s in strs}
            if len(ch)==1:
                prefix+=ch.pop()
            else:
                break

        return prefix
                