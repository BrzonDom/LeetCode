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


def Slt01_BldBnTls_Prt(Bn1, Bn2):

    print(f"\t1. Binary: {Bn1}")
    print(f"\t2. Binary: {Bn2}")
    print()

    nm1 = int(Bn1, 2)
    nm2 = int(Bn2, 2)

    bn1 = bin(nm1)
    bn2 = bin(nm2)

    print(f"\t\t1. Int Binary: {bn1[2:]} = {nm1}")
    print(f"\t\t2. Int Binary: {bn2[2:]} = {nm2}")
    print()

    bnRs = bin(nm1 + nm2)

    print(f"\tBinary result: {bnRs[2:]}")

    return bnRs[2:]


if __name__ == "__main__":

    InputLst = [["11", "1"],
                ["1010", "1011"]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Bn1 = case[0]
        Bn2 = case[1]

        print(f"\t1. Binary: {Bn1}")
        print(f"\t2. Binary: {Bn2}")
        print()

        nm1 = int(Bn1, 2)
        nm2 = int(Bn2, 2)

        bn1 = bin(nm1)
        bn2 = bin(nm2)

        print(f"\t\t1. Int Binary: {bn1[2:]} = {nm1}")
        print(f"\t\t2. Int Binary: {bn2[2:]} = {nm2}")
        print()

        nmRs = nm1 + nm2
        bnRs = bin(nmRs)

        print(f"\tBinary result: {bnRs[2:]} = {nmRs}")

        print("\n")
