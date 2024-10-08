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


def Hlp01_CnvBrd(Brd):

    BrdNm = [[0 for c in range(9)] for r in range(9)]

    for r, ln in enumerate(Brd):

        for c, nm in enumerate(ln):

            if nm == '.':
                Brd[r][c] = ' '

            else:
                BrdNm[r][c] = int(nm)

    return Brd, BrdNm


def Prt01_ShwBrd(Brd, nSpc=2):

    spc = nSpc * '\t'

    print(f"{spc}╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")

    for r, ln in enumerate(Brd):
        print(f"{spc}", end="║")

        for c, nm in enumerate(ln):

            if nm in ['.', ' ', 0]:
                print("   ", end="")

            else:
                print(f" {nm} ", end="")

            if c == 2 or c == 5:
                print("║", end="")

            elif c == 8:
                print("║")

            else:
                print("│", end="")

        if r == 2 or r == 5:
            print(f"{spc}╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")

        elif r == 8:
            print(f"{spc}╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")

            print()

        else:
            print(f"{spc}╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")


def Slt01_RwClBxCss_Prt(Brd):

    rows = {}
    cols = {}
    boxs = {}

    Valid = True

    for r, ln in enumerate(Brd):

        for c, nm in enumerate(ln):

            if '1' <= nm <= '9':

                if (r + 1) in rows:

                    if nm in rows[r + 1]:
                        print(f"\t\tDuplicate of {nm} at the {r + 1}. Row")

                        Valid = False

                    rows[r + 1] += nm

                else:
                    rows[r + 1] = nm

                if (c + 1) in cols:

                    if nm in cols[c + 1]:
                        print(f"\t\tDuplicate of {nm} at the {c + 1}. Column")

                        Valid = False

                    cols[c + 1] += nm

                else:
                    cols[c + 1] = nm

                if r <= 2:

                    if c <= 2:
                        b = 1

                        if b in boxs:

                            if nm in boxs[b]:
                                print(f"\t\tDuplicate of {nm} at the {b}. Sub-Box")

                                Valid = False

                            boxs[b] += nm

                        else:
                            boxs[b] = nm

                    elif c <= 5:
                        b = 2

                        if b in boxs:

                            if nm in boxs[b]:
                                print(f"\t\tDuplicate of {nm} at the {b}. Sub-Box")

                                Valid = False

                            boxs[b] += nm

                        else:
                            boxs[b] = nm

                    elif c <= 8:
                        b = 3

                        if b in boxs:

                            if nm in boxs[b]:
                                print(f"\t\tDuplicate of {nm} at the {b}. Sub-Box")

                                Valid = False

                            boxs[b] += nm

                        else:
                            boxs[b] = nm

                elif r <= 5:

                    if c <= 2:
                        b = 4

                        if b in boxs:

                            if nm in boxs[b]:
                                print(f"\t\tDuplicate of {nm} at the {b}. Sub-Box")

                                Valid = False

                            boxs[b] += nm

                        else:
                            boxs[b] = nm

                    elif c <= 5:
                        b = 5

                        if b in boxs:

                            if nm in boxs[b]:
                                print(f"\t\tDuplicate of {nm} at the {b}. Sub-Box")

                                Valid = False

                            boxs[b] += nm

                        else:
                            boxs[b] = nm

                    elif c <= 8:
                        b = 6

                        if b in boxs:

                            if nm in boxs[b]:
                                print(f"\t\tDuplicate of {nm} at the {b}. Sub-Box")

                                Valid = False

                            boxs[b] += nm

                        else:
                            boxs[b] = nm

                elif r <= 8:

                    if c <= 2:
                        b = 7

                        if b in boxs:

                            if nm in boxs[b]:
                                print(f"\t\tDuplicate of {nm} at the {b}. Sub-Box")

                                Valid = False

                            boxs[b] += nm

                        else:
                            boxs[b] = nm

                    elif c <= 5:
                        b = 8

                        if b in boxs:

                            if nm in boxs[b]:
                                print(f"\t\tDuplicate of {nm} at the {b}. Sub-Box")

                                Valid = False

                            boxs[b] += nm

                        else:
                            boxs[b] = nm

                    elif c <= 8:
                        b = 9

                        if b in boxs:

                            if nm in boxs[b]:
                                print(f"\t\tDuplicate of {nm} at the {b}. Sub-Box")

                                Valid = False

                            boxs[b] += nm

                        else:
                            boxs[b] = nm

    if Valid:
        print("\tSudoku is Valid")

        return True

    else:
        print()

        print("\tSudoku is Not Valid")

        return False


if __name__ == "__main__":

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

        Brd, BrdNm = Hlp01_CnvBrd(case)

        print("\tSet Board:")
        print()

        Prt01_ShwBrd(Brd)

        Slt01_RwClBxCss_Prt(case)

        print("\n")
