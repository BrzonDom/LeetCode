"""
39. Combination Sum

https://leetcode.com/problems/combination-sum/description/

    Given an array of distinct integers candidates and a target integer target, return a list of all unique
    combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
    frequency of at least one of the chosen numbers is different.

    The test cases are generated such that the number of unique combinations that sum up to target is less than 150
    combinations for the given input.


    Example 1:

        Input: candidates = [2, 3, 6, 7], target = 7
        Output: [[2, 2, 3], [7]]

        Explanation:
            2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
            7 is a candidate, and 7 = 7.
            These are the only two combinations.

    Example 2:

        Input: candidates = [2, 3, 5], target = 8
        Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

    Example 3:

        Input: candidates = [2], target = 1
        Output: []


    Constraints:

        1 <= candidates.length <= 30
        2 <= candidates[i] <= 40
        All elements of candidates are distinct.
        1 <= target <= 40

"""


def Slt01_SrtdCmbFnc_Prt(Cnds, Trg):

    def Hlp01_SrtdCmbRcr(cmb, ttl):

        if ttl == Trg:
            AllCmb.append(cmb)

            cmb.sort()

            if cmb not in Cmbs:
                Cmbs.append(cmb)

        elif ttl < Trg:
            AllCmb.append(cmb)

            for nm in Cnds:
                nCmb = cmb + [nm]
                nTtl = ttl + nm

                Hlp01_SrtdCmbRcr(nCmb, nTtl)

    print(f"\tCandidates: {Cnds}")
    print(f"\tTarget:      {Trg}")
    print()

    AllCmb = []
    Cmbs = []

    for nm in Cnds:
        Hlp01_SrtdCmbRcr([nm], nm)

    if AllCmb:

        print("\t\tAll Combinations:")

        fndCmb = False

        for cmb in AllCmb:
            ttl = sum(cmb)

            if ttl == Trg:

                if not fndCmb:
                    print()
                print(f"\t\t\t\t{cmb}")
                print()

                fndCmb = True

            else:
                print(f"\t\t\t{cmb} = {ttl}")

                fndCmb = False

        if not fndCmb:
            print()

    return Cmbs


def Slt02_VstdCmbFnc_Prt(Cnds, Trg):

    def Hlp02_VstdCmbRcr(cmb, ttl):

        if ttl == Trg:
            AllCmbs.append(cmb)

            Cmbs.append(cmb)

        elif ttl < Trg:
            AllCmbs.append(cmb)

            for nm in Cnds:

                nCmb = sorted(cmb + [nm])
                nTtl = ttl + nm

                if str(nCmb) not in Vstd:
                    Vstd.add(str(nCmb))

                    Hlp02_VstdCmbRcr(nCmb, nTtl)

    print(f"\tCandidates: {Cnds}")
    print(f"\tTarget:      {Trg}")
    print()

    Cmbs = []

    Vstd = set()
    AllCmbs = []

    for nm in Cnds:
        Hlp02_VstdCmbRcr([nm], nm)

    if AllCmbs:
        print("\t\tAll Combinations:")

        fndCmb = False

        for cmb in AllCmbs:
            ttl = sum(cmb)

            if ttl == Trg:

                if not fndCmb:
                    print()
                print(f"\t\t\t\t{cmb}")
                print()

                fndCmb = True

            else:
                print(f"\t\t\t{cmb} = {ttl}")

                fndCmb = False

        if not fndCmb:
            print()

    return Cmbs


def Hlp03_BckTrcCndRcr(cmb, ttl, idx):

    if ttl == Trg:
        AllCmbs.append(cmb)

        Cmbs.append(cmb)

    elif ttl < Trg and idx < len(Cnds):
        AllCmbs.append(cmb)

        nm = Cnds[idx]

        nCmb = cmb + [nm]
        nTtl = ttl + nm
        nIdx = idx + 1

        Hlp03_BckTrcCndRcr(nCmb, nTtl, idx)

        Hlp03_BckTrcCndRcr(cmb, ttl, nIdx)


def Slt03_BckTrcCndRcrFnc_Prt(Cnds, Trg):

    def Hlp03_BckTrcCndRcr(cmb, ttl, idx):

        if ttl == Trg:
            AllCmbs.append(cmb)

            Cmbs.append(cmb)

        elif ttl < Trg and idx < len(Cnds):
            AllCmbs.append(cmb)

            nm = Cnds[idx]

            nCmb = cmb + [nm]
            nTtl = ttl + nm
            nIdx = idx + 1

            Hlp03_BckTrcCndRcr(nCmb, nTtl, idx)

            Hlp03_BckTrcCndRcr(cmb, ttl, nIdx)

    print(f"\tCandidates: {Cnds}")
    print(f"\tTarget:      {Trg}")
    print()

    Cmbs = []
    AllCmbs = []

    Hlp03_BckTrcCndRcr([], 0, 0)

    if Cmbs:
        print("\tCombinations:")

        for cmb in Cmbs:
            print(f"\t\t{cmb}")

    else:
        print("\tNo Combinations found")


def Out_Prt(Cmbs):

    if Cmbs:
        print("\tCombinations:")

        for c, cmb in enumerate(Cmbs):
            print(f"\t\t{c+1}. {cmb}")

    else:
        print("\tNo Combinations found")


if __name__ == "__main__":

    InputLst = [[[2, 3, 6, 7], 7],
                [[2, 3, 5], 8],
                [[2], 1]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        # outRtrn = Slt01_SrtdCmbFnc_Prt(case[0], case[1])

        # outRtrn = Slt02_VstdCmbFnc_Prt(case[0], case[1])

        Cnds = case[0]
        Trg = case[1]

        print(f"\tCandidates: {Cnds}")
        print(f"\tTarget:      {Trg}")
        print()

        Cmbs = []
        AllCmbs = []

        Hlp03_BckTrcCndRcr([], 0, 0)

        print("\t\tAll Combinations:")

        for cmb in AllCmbs:
            print(f"\t\t\t{cmb}")
        print()

        if Cmbs:
            print("\tCombinations:")

            for cmb in Cmbs:
                print(f"\t\t{cmb}")

        else:
            print("\tNo Combinations found")

        # Out_Prt(outRtrn)

        print("\n")
