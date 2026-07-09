class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = {}
        for i in range(9):
            squares[i] = []

        # Check rows and collect square values
        for i in range(9):
            row = [0] * 9

            for j in range(9):
                if board[i][j].isdigit():
                    num = int(board[i][j]) - 1

                    row[num] += 1
                    if row[num] == 2:
                        return False

                    if 0 <= i <= 2 and 0 <= j <= 2:
                        squares[0].append(board[i][j])
                    elif 0 <= i <= 2 and 3 <= j <= 5:
                        squares[1].append(board[i][j])
                    elif 0 <= i <= 2 and 6 <= j <= 8:
                        squares[2].append(board[i][j])
                    elif 3 <= i <= 5 and 0 <= j <= 2:
                        squares[3].append(board[i][j])
                    elif 3 <= i <= 5 and 3 <= j <= 5:
                        squares[4].append(board[i][j])
                    elif 3 <= i <= 5 and 6 <= j <= 8:
                        squares[5].append(board[i][j])
                    elif 6 <= i <= 8 and 0 <= j <= 2:
                        squares[6].append(board[i][j])
                    elif 6 <= i <= 8 and 3 <= j <= 5:
                        squares[7].append(board[i][j])
                    elif 6 <= i <= 8 and 6 <= j <= 8:
                        squares[8].append(board[i][j])

        # Check columns
        for j in range(9):
            col = [0] * 9

            for i in range(9):
                if board[i][j].isdigit():
                    num = int(board[i][j]) - 1

                    col[num] += 1
                    if col[num] == 2:
                        return False

        # Check 3x3 squares
        for k, v in squares.items():
            seen = set()

            for digit in v:
                if digit in seen:
                    return False
                else:
                    seen.add(digit)

        return True
            
        


                

        