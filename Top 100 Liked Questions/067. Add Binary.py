"""
67. Add Binary

https://leetcode.com/problems/add-binary/description/


    Given two binary strings a and b, return their sum as a binary string.


    Example 1:

        Input: a = "11", b = "1"

        Output: "100"

    Example 2:

        Input: a = "1010", b = "1011"

        Output: "10101"


    Constraints:

        1 <= a.length, b.length <= 10^4
        a and b consist only of '0' or '1' characters.
        Each string does not contain leading zeros except for the zero itself.

"""


if __name__ == "__main__":

    InputLst = [["11", "1"],
                ["1010", "1011"]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Bn1 = case[0]
        Bn2 = case[1]

        print(f"\t{Bn1}")
        print(f"\t{Bn2}")

        print("\n")
