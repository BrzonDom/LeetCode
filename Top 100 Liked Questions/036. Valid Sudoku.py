"""
36. Valid Sudoku

https://leetcode.com/problems/valid-sudoku/description/


    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to
    the following rules:

        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Note:
        - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        - Only the filled cells need to be validated according to the mentioned rules.


    Example 1:

        Input: board =
                    [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        Output: true

    Example 2:

        Input: board =
                    [["8", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        Output: false

        Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there
            are two 8's in the top left 3x3 sub-box, it is invalid.


    Constraints:

        board.length == 9
        board[i].length == 9
        board[i][j] is a digit 1-9 or '.'.

"""


InputLst = [[["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
            [["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt + 1}.Case\n")

    print("\tSudoku:")

    rows = {}
    cols = {}
    boxs = {}

    isValid = True

    for r, row in enumerate(case):
        print("\n\t\t", end="")

        for c, col in enumerate(row):
            print(col, end=" ")

            if '1' <= col <= '9':

                if (r+1) not in rows:
                    rows[r+1] = col

                else:
                    rows[r+1] += col

                if (c+1) not in cols:
                    cols[c+1] = col

                else:
                    cols[c+1] += col

                if r <= 2:

                    if c <= 2:

                        if 1 not in boxs:
                            boxs[1] = col

                        else:
                            boxs[1] += col

                    elif c <= 5:

                        if 2 not in boxs:
                            boxs[2] = col

                        else:
                            boxs[2] += col

                    elif c <= 8:

                        if 3 not in boxs:
                            boxs[3] = col

                        else:
                            boxs[3] += col

                elif r <= 5:

                    if c <= 2:

                        if 4 not in boxs:
                            boxs[4] = col

                        else:
                            boxs[4] += col

                    elif c <= 5:

                        if 5 not in boxs:
                            boxs[5] = col

                        else:
                            boxs[5] += col

                    elif c <= 8:

                        if 6 not in boxs:
                            boxs[6] = col

                        else:
                            boxs[6] += col

                elif r <= 8:

                    if c <= 2:

                        if 7 not in boxs:
                            boxs[7] = col

                        else:
                            boxs[7] += col

                    elif c <= 5:

                        if 8 not in boxs:
                            boxs[8] = col

                        else:
                            boxs[8] += col

                    elif c <= 8:

                        if 9 not in boxs:
                            boxs[9] = col

                        else:
                            boxs[9] += col

    print("\n")
