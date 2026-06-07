class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        
        return "".join(parts)
    
    def decode(self, s: str) -> List[str]:
        idx = 0
        result = []

        while idx<len(s):
            ln=[]
            while idx<len(s) and s[idx].isdigit():
                ln.append(s[idx])
                idx+=1
            
            if idx < len(s) and s[idx]=='#':
                idx+=1
            
            ln = int("".join(ln))
            string = s[idx:idx+ln]
            idx += ln

            result.append(string)

        return result