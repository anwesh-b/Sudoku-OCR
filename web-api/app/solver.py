import numbers

M = 9


def validate_game(game):
    """
    Check if game is array of size 9 and each row is array of size 9 and each item is number type
    """
    if len(game) != 9:
        return False
    for row in game:
        if len(row) != 9:
            return False
        for item in row:
            if not isinstance(item, numbers.Number):
                return False
    return True


def puzzle(a):
    """
    Print the puzzle
    """
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()


def solve(grid, row, col, num):
    """
    Solve the puzzle
    """
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True


def sudoku(grid, row, col):
    """
    Main function to solve the puzzle
    """
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return sudoku(grid, row, col + 1)
    for num in range(1, M + 1, 1):
        if solve(grid, row, col, num):
            grid[row][col] = num
            if sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
