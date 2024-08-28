"""
1905. Count Sub Islands

https://leetcode.com/problems/count-sub-islands/description/?envType=daily-question&envId=2024-08-28

    You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's
    (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells
    outside of the grid are considered water cells.

    An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make
    up this island in grid2.

    Return the number of islands in grid2 that are considered sub-islands.


    Example 1:

        Input:
            grid1 = [[1, 1, 1, 0, 0],
                     [0, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0],
                     [1, 1, 0, 1, 1]],

            grid2 = [[1, 1, 1, 0, 0],
                     [0, 0, 1, 1, 1],
                     [0, 1, 0, 0, 0],
                     [1, 0, 1, 1, 0],
                     [0, 1, 0, 1, 0]]
        Output: 3

        Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
            The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.

    Example 2:

        Input:
            grid1 = [[1, 0, 1, 0, 1],
                     [1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1],
                     [1, 0, 1, 0, 1]],

            grid2 = [[0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1],
                     [0, 1, 0, 1, 0],
                     [0, 1, 0, 1, 0],
                     [1, 0, 0, 0, 1]]

        Output: 2

        Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
            The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.


    Constraints:

        m == grid1.length == grid2.length
        n == grid1[i].length == grid2[i].length
        1 <= m, n <= 500
        grid1[i][j] and grid2[i][j] are either 0 or 1

"""

"""
Symbols:
    Water = [ ]
    Land  = [#]
"""


if __name__ == "__main__":

    InputLst = [[
            [[1, 1, 1, 0, 0],
             [0, 1, 1, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 1, 1]],
            [[1, 1, 1, 0, 0],
             [0, 0, 1, 1, 1],
             [0, 1, 0, 0, 0],
             [1, 0, 1, 1, 0],
             [0, 1, 0, 1, 0]]
        ], [
            [[1, 0, 1, 0, 1],
             [1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [1, 0, 1, 0, 1]],
            [[0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1],
             [0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0],
             [1, 0, 0, 0, 1]]
                ]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Lnd = case[0]
        Isl = case[1]

        RwDm = len(Lnd)
        ClDm = len(Lnd[0])

        print("\tLand grid:")

        for ln in Lnd:
            print("\t\t", end="")

            for sq in ln:

                if sq:
                    print("[#]", end="")
                else:
                    print("[ ]", end="")
            print()
        print()

        print("\tIsland grid:")

        for ln in Isl:
            print("\t\t", end="")

            for sq in ln:

                if sq:
                    print("[#]", end="")
                else:
                    print("[ ]", end="")
            print()
        print()

        print("\tGrid dimensions:")
        print(f"\t\tRows: {RwDm}")
        print(f"\t\tCols: {ClDm}")
        print()

        Mvmt = {}

        for r, ln in enumerate(Lnd):
            for c, sq in enumerate(ln):

                if c > 0 and Lnd[r][c - 1]:

                    if (r, c) not in Mvmt:
                        Mvmt[(r, c)] = {"L": True,
                                        "U": False,
                                        "R": False,
                                        "D": False}

                    else:
                        Mvmt[(r, c)]["L"] = True

                if r > 0 and Lnd[r-1][c]:

                    if (r, c) not in Mvmt:
                        Mvmt[(r, c)] = {"L": False,
                                        "U": True,
                                        "R": False,
                                        "D": False}

                    else:
                        Mvmt[(r, c)]["U"] = True

                if c < ClDm-1 and Lnd[r][c+1]:

                    if (r, c) not in Mvmt:
                        Mvmt[(r, c)] = {"L": False,
                                        "U": False,
                                        "R": True,
                                        "D": False}

                    else:
                        Mvmt[(r, c)]["R"] = True

                if r < RwDm-1 and Lnd[r+1][c]:

                    if (r, c) not in Mvmt:
                        Mvmt[(r, c)] = {"L": False,
                                        "U": False,
                                        "R": False,
                                        "D": True}

                    else:
                        Mvmt[(r, c)]["D"] = True

        print("\t\tLand with a move:\n")
        print(f"\t\t\t\t\t\t  L   U   R   D")

        for r, ln in enumerate(Lnd):
            for c, sq in enumerate(ln):

                if (r, c) in Mvmt:
                    print(f"\t\t\t{[r, c]}: ", end="\t|")

                    if Mvmt[(r, c)]["L"]:
                        print(" x ", end="|")
                    else:
                        print("   ", end="|")

                    if Mvmt[(r, c)]["U"]:
                        print(" x ", end="|")
                    else:
                        print("   ", end="|")

                    if Mvmt[(r, c)]["R"]:
                        print(" x ", end="|")
                    else:
                        print("   ", end="|")

                    if Mvmt[(r, c)]["D"]:
                        print(" x ", end="|")
                    else:
                        print("   ", end="|")

                    print()

        print("\n")
