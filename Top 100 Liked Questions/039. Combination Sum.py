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

    def Hlp01_SrtdCmbRcrs(cmb, ttl):

        AllCmb.append(cmb)

        if ttl == Trg:
            cmb.sort()

            if cmb not in Cmbs:
                Cmbs.append(cmb)

        elif ttl < Trg:

            for nm in Cnds:
                nCmb = cmb + [nm]
                nTtl = ttl + nm

                Hlp01_SrtdCmbRcrs(nCmb, nTtl)

    print(f"\tCandidates: {Cnds}")
    print(f"\tTarget:      {Trg}")
    print()

    AllCmb = []
    Cmbs = []

    print("\t\tAll viable combination:")

    for nm in Cnds:
        Hlp01_SrtdCmbRcrs([nm], nm)

    print()

    if Cmbs:
        print("\tCombinations:")

        for c, cmb in enumerate(Cmbs):
            print(f"\t\t{c + 1}. {cmb}")

        return Cmbs

    else:
        print("\tNo Combinations found")

        return Cmbs


if __name__ == "__main__":

    InputLst = [[[2, 3, 6, 7], 7],
                [[2, 3, 5], 8],
                [[2], 1]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Slt01_SrtdCmbFnc_Prt(case[0], case[1])

        print("\n")
