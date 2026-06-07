import json
class Solution:

    def encode(self, strs: List[str]) -> str:
        mp = dict()
        for i,s in enumerate(strs):
            mp[i] = s
        return json.dumps(mp)
    
    def decode(self, s: str) -> List[str]:
        mp = json.loads(s)
        print(mp)
        return list(mp.values())