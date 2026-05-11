class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s = deque(s)

        for direction,steps in shift:
            while steps:
                if direction==0:
                    s.append(s.popleft())
                    steps-=1
                else:
                    s.appendleft(s.pop())
                    steps-=1
            
        return "".join(s)