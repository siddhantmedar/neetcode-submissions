class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = [arr[-1]]
        result = [-1]

        for i in range(len(arr)-2,-1,-1):
            ele = arr[i]

            result.append(stack[-1])

            while stack and stack[-1] < ele:
                stack.pop()
            
            if not stack:
                stack.append(ele)

        return result[::-1]
