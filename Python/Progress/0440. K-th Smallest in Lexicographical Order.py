"""
440. K-th Smallest in Lexicographical Order

https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/


    Given two integers n and k, return the k^th lexicographically smallest integer in the range [1, n].


    Example 1:

        Input: n = 13, k = 2

        Output: 10

        Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the
            second smallest number is 10.

    Example 2:

        Input: n = 1, k = 1

        Output: 1


    Constraints:

        1 <= k <= n <= 10^9


    Topics:

        Trie


    Courses:

        Daily: 2024/09/22

"""


if __name__ == "__main__":

    InputLst = [[13, 2],
                [1, 1]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        print(f"\t{case[0]}")
        print(f"\t{case[1]}")

        print("\n")
