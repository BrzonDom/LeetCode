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
import copy

"""
Symbols:
    Water     = [ ]
    Land      = [#]
    Connected = {#}
"""


def Prt01_Grd_DspIn(Grd, Tp, spc=1):

    spc = spc * "\t"

    rwGr = len(Grd)
    clGr = len(Grd[0])

    print(f"{spc}{Tp} grid:")

    print(f"{spc}\t\t\t", end="   ")
    for c in range(1, clGr + 1):
        print(f"{c:2}", end=" ")
    print()

    for r, ln in enumerate(Grd):
        print(f"{spc}\t\t\t{r + 1:2}", end=" ")

        for sq in ln:

            if sq == 1:
                print("[#]", end="")

            elif sq == 2:
                print("{#}", end="")

            else:
                print("[ ]", end="")

        print()
    print()


def Prt02_Grd_DspDt(Grd, Dt, spc=2):

    spc = "\t" * spc

    print(f"{spc}Land moves:\n")
    print(f"{spc}\t\t\t\t  L   U   R   D")

    for r, ln in enumerate(Grd):
        for c, sq in enumerate(ln):

            r += 1
            c += 1

            if (r, c) in Dt:
                print(f"{spc}\t{[r, c]}: ", end="\t|")

                if Dt[(r, c)]["L"]:
                    print(" x ", end="|")
                else:
                    print("   ", end="|")

                if Dt[(r, c)]["U"]:
                    print(" x ", end="|")
                else:
                    print("   ", end="|")

                if Dt[(r, c)]["R"]:
                    print(" x ", end="|")
                else:
                    print("   ", end="|")

                if Dt[(r, c)]["D"]:
                    print(" x ", end="|")
                else:
                    print("   ", end="|")

                print()


def Hlp01_FlFldWhlLp(Str, Grd, Vstd):

    rwGr = len(Grd)
    clGr = len(Grd[0])

    lnd = []
    flQu = [Str]

    while flQu:
        (r, c) = flQu.pop(0)

        Vstd.add((r, c))
        lnd.append((r, c))

        if c > 0 and Grd[r][c - 1] and (r, c - 1) not in Vstd:
            flQu.append((r, c - 1))

        if r > 0 and Grd[r - 1][c] and (r - 1, c) not in Vstd:
            flQu.append((r - 1, c))

        if c < clGr - 1 and Grd[r][c + 1] and (r, c + 1) not in Vstd:
            flQu.append((r, c + 1))

        if r < rwGr - 1 and Grd[r + 1][c] and (r + 1, c) not in Vstd:
            flQu.append((r + 1, c))

    return lnd, Vstd


def Hlp01_FlFldWhlLp_Prt(Str, Grd, Vstd):

    dmRw = len(Grd)
    dmCl = len(Grd[0])

    lnd = []
    flQu = [Str]

    crLnd = copy.deepcopy(Grd)

    while flQu:
        (r, c) = flQu.pop(0)

        Vstd.add((r, c))
        lnd.append((r, c))

        crLnd[r][c] = 2

        if c > 0 and Grd[r][c - 1] and (r, c - 1) not in Vstd:
            flQu.append((r, c - 1))

        if r > 0 and Grd[r - 1][c] and (r - 1, c) not in Vstd:
            flQu.append((r - 1, c))

        if c < dmCl - 1 and Grd[r][c + 1] and (r, c + 1) not in Vstd:
            flQu.append((r, c + 1))

        if r < dmRw - 1 and Grd[r + 1][c] and (r + 1, c) not in Vstd:
            flQu.append((r + 1, c))

    Prt01_Grd_DspIn(crLnd, f"{ilCnt+1}. Connected land", 2)

    return lnd, Vstd


def Hlp02_FndIslWtFlFldMtd(Grd):

    islns = []
    vstd = set()

    for r, ln in enumerate(Grd):
        for c, sq in enumerate(ln):

            if sq and (r, c) not in vstd:

                ilnd, vstd = Hlp01_FlFldWhlLp((r, c), Grd, vstd)

                islns.append(ilnd)

    return islns


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

        dmRw = len(Lnd)
        dmCl = len(Lnd[0])

        Prt01_Grd_DspIn(Lnd, "Land")

        Prt01_Grd_DspIn(Isl, "Island")

        print()

        print("\tGrid dimensions:")
        print(f"\t\tRows: {dmRw}")
        print(f"\t\tCols: {dmCl}")
        print()

        """

        Mvmt = {}

        for r, ln in enumerate(Lnd):
            for c, sq in enumerate(ln):

                if sq:
                    if c > 0 and Lnd[r][c - 1]:

                        if (r+1, c+1) not in Mvmt:
                            Mvmt[(r+1, c+1)] = {"L": True,
                                                "U": False,
                                                "R": False,
                                                "D": False}

                        else:
                            Mvmt[(r+1, c+1)]["L"] = True

                    if r > 0 and Lnd[r-1][c]:

                        if (r+1, c+1) not in Mvmt:
                            Mvmt[(r+1, c+1)] = {"L": False,
                                                "U": True,
                                                "R": False,
                                                "D": False}

                        else:
                            Mvmt[(r+1, c+1)]["U"] = True

                    if c < dmCl-1 and Lnd[r][c+1]:

                        if (r+1, c+1) not in Mvmt:
                            Mvmt[(r+1, c+1)] = {"L": False,
                                                "U": False,
                                                "R": True,
                                                "D": False}

                        else:
                            Mvmt[(r+1, c+1)]["R"] = True

                    if r < dmRw-1 and Lnd[r+1][c]:

                        if (r+1, c+1) not in Mvmt:
                            Mvmt[(r+1, c+1)] = {"L": False,
                                                "U": False,
                                                "R": False,
                                                "D": True}

                        else:
                            Mvmt[(r+1, c+1)]["D"] = True

                    if (r + 1, c + 1) not in Mvmt:
                        Mvmt[(r + 1, c + 1)] = {"L": False,
                                                "U": False,
                                                "R": False,
                                                "D": False}

        Prt02_Grd_DspDt(Lnd, Mvmt)
        
        """

        ilLnds = Hlp02_FndIslWtFlFldMtd(Lnd)

        # ilLnds = []
        #
        # ilCnt = 0
        #
        # vstd = set()
        #
        # for r, ln in enumerate(Lnd):
        #     for c, sq in enumerate(ln):
        #
        #         if sq and (r, c) not in vstd:
        #
        #             ilnd, vstd = Hlp01_FlFldWhlLp((r, c), Lnd, vstd)
        #
        #             # ilnd, vstd = Hlp01_FlFldWhlLp_Prt((r, c), Lnd, vstd)
        #
        #             ilLnds.append(ilnd)
        #
        #             ilCnt += 1

        ilIsls = []
        ilCnt = 0

        vstd = set()

        for r, ln in enumerate(Isl):
            for c, sq in enumerate(ln):

                if sq and (r, c) not in vstd:

                    ilnd, vstd = Hlp01_FlFldWhlLp((r, c), Isl, vstd)

                    # ilnd, vstd = Hlp01_FlFldWhlLp_Prt((r, c), Isl, vstd)

                    ilIsls.append(ilnd)

                    ilCnt += 1

        print("\tLand islands:")
        for isl in ilLnds:
            print(f"\t\t{isl}")
        print()

        print("\tIslands:")
        for isl in ilIsls:
            print(f"\t\t{isl}")

        print("\n")
