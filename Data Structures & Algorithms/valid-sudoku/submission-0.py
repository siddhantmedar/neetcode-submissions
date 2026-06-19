class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)

        # row
        for i in range(N):
            seen = set()
            for ele in board[i]:
                if ele==".":
                    continue
                if ele in seen or not 1<=int(ele)<=9:
                    return False
                seen.add(ele)

        for j in range(N):
            seen = set()
            for i in range(N):
                ele = board[i][j]
                if ele==".":
                    continue
                if ele in seen or not 1<=int(ele)<=9:
                    return False
                seen.add(ele)

        # row: 0,3,6
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                seen = set()
                for row in range(i,i+3):
                    for col in range(j,j+3):
                        ele = board[row][col]
                        if ele==".":
                            continue
                        if ele in seen or not 1<=int(ele)<=9:
                            return False
                        seen.add(ele)
        
        return True

