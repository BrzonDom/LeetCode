"""
1137. N-th Tribonacci Number

https://leetcode.com/problems/n-th-tribonacci-number/description/


    The Tribonacci sequence T_n is defined as follows:

    T_0 = 0, T_1 = 1, T_2 = 1, and T_(n+3) = T_n + T_(n+1) + T_(n+2) for n >= 0.

    Given n, return the value of T_n.


    Example 1:

        Input: n = 4

        Output: 4

        Explanation:
            T_3 = 0 + 1 + 1 = 2
            T_4 = 1 + 1 + 2 = 4

    Example 2:

        Input: n = 25

        Output: 1389537


    Constraints:

        0 <= n <= 37
        The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.


    Topics:

        Math
        Dynamic Programming
        Memoization


    Courses:

        LeetCode 75

"""


if __name__ == '__main__':

    Input_Lst = [4, 25]

    for cs_cnt, case in enumerate(Input_Lst, start=1):

        print(f"{cs_cnt}. Case\n")

        print(f"\tn: {case}")

        trb_num_lst = [0, 1, 1]

        if case < 3:
            print(case)
        else:
            for i in range(3, case + 1):
                trb_num_lst[0], trb_num_lst[1], trb_num_lst[2] = trb_num_lst[1], trb_num_lst[2], sum(trb_num_lst)
            print(trb_num_lst[2])

        print("\n")
