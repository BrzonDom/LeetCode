"""
40. Combination Sum II

https://leetcode.com/problems/combination-sum-ii/description/

    Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations
    in candidates where the candidate numbers sum to target.

    Each number in candidates may only be used once in the combination.

    Note: The solution set must not contain duplicate combinations.


    Example 1:

        Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
        Output:
            [[1, 1, 6],
             [1, 2, 5],
             [1, 7],
             [2, 6]]

    Example 2:

        Input: candidates = [2, 5, 2, 1, 2], target = 5
        Output:
            [[1, 2, 2],
             [5]]


Constraints:

    1 <= candidates.length <= 100
    1 <= candidates[i] <= 50
    1 <= target <= 30

"""


def Slt01_SrtdCmbFnc_Prt(Cnds, Trg):

    def Hlp01_SrtdCmbRcrs(cmb, cnd, ttl):

        if ttl == Trg:
            AllCmbs.append(cmb)

            cmb.sort()

            if cmb not in Cmbs:
                Cmbs.append(cmb)

        elif ttl < Trg:
            AllCmbs.append(cmb)

            for n, nm in enumerate(cnd):
                nCmb = cmb + [nm]
                nTtl = ttl + nm
                nCnd = cnd[:n] + cnd[n + 1:]

                Hlp01_SrtdCmbRcrs(nCmb, nCnd, nTtl)

    print(f"\tCandidates: {Cnds}")
    print(f"\tTarget:      {Trg}")
    print()

    Cmbs = []
    AllCmbs = []

    for n, nm in enumerate(Cnds):
        Hlp01_SrtdCmbRcrs([nm], Cnds[:n] + Cnds[n + 1:], nm)

    if AllCmbs:

        print("\t\tAll Combinations:")

        fndCmb = False

        for cmb in AllCmbs:
            ttl = sum(cmb)

            if ttl == Trg:

                if not fndCmb:
                    print()
                print(f"\t\t\t{cmb}")
                print()

                fndCmb = True

            else:
                print(f"\t\t\t\t{cmb} = {ttl}")

                fndCmb = False

        if not fndCmb:
            print()

        if Cmbs:
            print("\tCombinations:")

            for cmb in Cmbs:
                print(f"\t\t{cmb}")

            return Cmbs

    print("\tNo Combinations Found")

    return []


if __name__ == "__main__":

    InputLst = [[[10, 1, 2, 7, 6, 1, 5], 8],
                [[2, 5, 2, 1, 2], 5]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Slt01_SrtdCmbFnc_Prt(case[0], case[1])

        print("\n")
