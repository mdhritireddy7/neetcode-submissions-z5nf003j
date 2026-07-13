class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def backtracking(i, row, col):
            if i == len(word):
                return True

            if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols) 
                or (word[i] != board[row][col]) or ((row, col) in visited)):
                return False

            visited.add((row, col))

            found = ((backtracking(i + 1, row + 1, col)) or
                    (backtracking(i + 1, row - 1, col)) or
                    (backtracking(i + 1, row, col + 1)) or
                    (backtracking(i + 1, row, col - 1)))

            visited.remove((row, col))

            return found

        for r in range(rows):
            for c in range(cols):
                if backtracking(0, r, c):
                    return True

        return False
        