"""
1431. Kids With the Greatest Number of Candies

https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/


    There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number
    of candies the i^th kid has, and an integer extraCandies, denoting the number of extra candies that you have.

    Return a boolean array result of length n, where result[i] is true if, after giving the i^th kid all
    the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.


    Example 1:

        Input: candies = [2, 3, 5, 1, 3], extraCandies = 3

        Output: [true, true, true, false, true]

        Explanation: If you give all extraCandies to:
            - Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
            - Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
            - Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
            - Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
            - Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

    Example 2:

        Input: candies = [4, 2, 1, 1, 2], extraCandies = 1

        Output: [true, false, false, false, false]

        Explanation: There is only 1 extra candy.
            Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

    Example 3:

        Input: candies = [12, 1, 12], extraCandies = 10

        Output: [true, false, true]


    Constraints:

        n == candies.length
        2 <= n <= 100
        1 <= candies[i] <= 100
        1 <= extraCandies <= 50


    Topics:

        Array


    Courses:

        LeetCode 75

"""


def Slt01_Itr_ExtAdd_Prt(Cnds, Ext_Cnd):

    print(f"\tOriginal candies: {Cnds}")
    print(f"\tExtra candy: {Ext_Cnd}")
    print()

    mx_cnd = max(Cnds)

    print(f"\tOriginal max candy: {mx_cnd}")
    print()

    isMx_cnds = []

    print("\t\tCandies:")
    for idx, cnd in enumerate(Cnds):
        print(f"\t\t\t{idx + 1:2}. {cnd:3}")

        cr_cnd = cnd + Ext_Cnd

        if cr_cnd >= mx_cnd:
            isMx_cnds.append(True)
            print(f"\t\t\t\t{cr_cnd:3} = Max")

        else:
            isMx_cnds.append(False)
            print(f"\t\t\t\t{cr_cnd:3} = Not max")
    print()

    print(f"\tMax candies: {isMx_cnds}")

    return isMx_cnds


if __name__ == "__main__":

    InputLst = [[[2, 3, 5, 1, 3], 3],
                [[4, 2, 1, 1, 2], 1],
                [[12, 1, 12], 10]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Slt01_Itr_ExtAdd_Prt(case[0], case[1])

        print("\n")
