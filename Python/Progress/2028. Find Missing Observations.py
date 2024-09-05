"""
2028. Find Missing Observations

https://leetcode.com/problems/find-missing-observations/description/

        Daily: 2024/09/05

    You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went
    missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average
    value of the n + m rolls.

    You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also
    given the two integers mean and n.

    Return an array of length n containing the missing observations such that the average value of the n + m rolls is
    exactly mean. If there are multiple valid answers, return any of them. If no such array exists,
    return an empty array.

    The average value of a set of k numbers is the sum of the numbers divided by k.

    Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.


    Example 1:

        Input: rolls = [3, 2, 4, 3], mean = 4, n = 2

        Output: [6, 6]

        Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.

    Example 2:

        Input: rolls = [1, 5, 6], mean = 3, n = 4

        Output: [2, 3, 2, 2]

        Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.

    Example 3:

        Input: rolls = [1, 2, 3, 4], mean = 6, n = 4

        Output: []

        Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.


    Constraints:

        m == rolls.length
        1 <= n, m <= 10^5
        1 <= rolls[i], mean <= 6

"""
"""
    Tags:
    
        Array
        Math
        Simulation
"""


if __name__ == "__main__":

    InputLst = [[[3, 2, 4, 3], 4, 2],
                [[1, 5, 6], 3, 4],
                [[1, 2, 3, 4], 6, 4]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Rlls = case[0]
        Men = case[1]
        Mss = case[2]

        print(f"\tRolls:  {Rlls}")
        print(f"\tMean:    {Men}")
        print(f"\tMissing: {Mss}")
        print()

        rlCnt = len(Rlls)
        alCnt = rlCnt + Mss
        msCnt = Mss

        rlNmb = Rlls
        alNmb = Rlls + [0 for m in range(msCnt)]
        msNmb = [0 for m in range(msCnt)]

        rlTtl = sum(Rlls)
        alTtl = Men * alCnt
        msTtl = alTtl - rlTtl

        print("\tOriginal rolls:")
        print(f"\t\tRolls: {Rlls}")
        print(f"\t\tCount:  {rlCnt}")
        print(f"\t\tTotal:  {rlTtl}")

        print("\n")
