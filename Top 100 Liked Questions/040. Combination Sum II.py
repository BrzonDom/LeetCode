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


def Hlp01_SrtdCmbRcrs(cmb, cnd, ttl):

    if ttl == Trg:

        Cmbs.append(cmb)

    elif ttl < Trg:

        for n, nm in enumerate(cnd):

            print(f"\t\t{cmb + [nm]}")
            print(f"\t\t{ttl + nm}")
            print(f"\t\t{cnd[:n]} {cnd[n+1:]}")
            print()


if __name__ == "__main__":

    InputLst = [[[10, 1, 2, 7, 6, 1, 5], 8],
                [[2, 5, 2, 1, 2], 5]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Cnds = case[0]
        Trg = case[1]

        print(f"\tCandidates: {Cnds}")
        print(f"\tTarget:      {Trg}")
        print()

        Cmbs = []

        for n, nm in enumerate(Cnds):
            Hlp01_SrtdCmbRcrs([nm], Cnds[:n] + Cnds[n+1:], nm)
        print()

        print("\tCombinations:")

        for cmb in Cmbs:
            print(f"\t\t{cmb}")

        print("\n")
