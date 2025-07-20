from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        subbxs = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                elem = board[i][j]
                if elem != '.':
                    if elem in rows[i] or elem in columns[j] or elem in subbxs[(i//3, j//3)]:
                        return False
                    else:
                        rows[i].add(elem)
                        columns[j].add(elem)
                        subbxs[(i//3,j//3)].add(elem)
        return True   
