class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Boolean arrays to track if a number has appeared in a row, column, or 3x3 box
        rows = [[False] * 9 for _ in range(9)]  # Track numbers for each row
        cols = [[False] * 9 for _ in range(9)]  # Track numbers for each column
        boxes = [[False] * 9 for _ in range(9)] # Track numbers for each 3x3 box

        # Loop through each cell in the 9x9 board
        for i in range(9):  # Traverse each row (i is the row index)
            for j in range(9):  # Traverse each column (j is the column index)
                value = board[i][j]  # Get the current cell value
                if value == '.':
                    continue  # Skip empty cells ('.' represents empty)

                num = int(value) - 1  # Convert '1'-'9' to an integer range 0-8 for indexing
                boxIndex = (i // 3) * 3 + j // 3  # Calculate the index of the 3x3 box

                # Check if the current number has already appeared in the same row, column, or box
                if rows[i][num] or cols[j][num] or boxes[boxIndex][num]:
                    return False  # If it has appeared before, return false (invalid Sudoku)

                # Mark the current number as seen in the respective row, column, and 3x3 box
                rows[i][num] = cols[j][num] = boxes[boxIndex][num] = True

        return True  # If no duplicates are found, return true (valid Sudoku)
        