class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''

        for s in strs:
            string+=str(len(s))+"#"
            string+=s

        return string
    
    def decode(self, s: str) -> List[str]:
        idx = 0
        result = []

        while idx<len(s):
            ln=''
            while idx<len(s) and s[idx].isdigit():
                ln+=s[idx]
                idx+=1
            
            if s[idx]=='#':
                idx+=1
            
            ln = int(ln)
            string = s[idx:idx+ln]
            idx = idx+ln

            result.append(string)

        return result

        # 4 h e l l o 5 w o r l  d
        # 0 1 2 3 4 5 6 7 8 9 10 11
        #   _

        # 1+4=5  
        # 1+4
        # _
        #   h e l l o
        # 0 1 2 3 4 5


        # h i
        # _
        # 1+2