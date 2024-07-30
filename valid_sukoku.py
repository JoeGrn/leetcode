class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialise set for cols rows and squares which need to be checked for valid sudoku
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)


        # loop over each square
        for r in range(9):
            for c in range(9):
                # if the square is blank skip
                if board[r][c] == ".":
                    continue
                if(
                    # if a row contains an existing value exit False
                    board[r][c] in rows[r]
                    # if a col contains an existing value exit False
                    or board[r][c] in cols[c]
                    # if a square contains an existing value exit False
                    # use floor division to index squares e.g. 7 // 3 = 2
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                
                # add board value to col
                cols[c].add(board[r][c])
                # add board value to row
                rows[r].add(board[r][c])
                # add board value to square
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

        # O(9^2)