"""
1310. XOR Queries of a Subarray

https://leetcode.com/problems/xor-queries-of-a-subarray/description/


    You are given an array arr of positive integers. You are also given the array queries where
    queries[i] = [left_i, right_i].

    For each query i compute the XOR of elements from left_i to right_i
    (that is, arr[left_i] XOR arr[left_i + 1] XOR ... XOR arr[right_i]).

    Return an array answer where answer[i] is the answer to the i^th query.


    Example 1:

        Input: arr = [1, 3, 4, 8], queries = [[0, 1], [1, 2], [0, 3], [3, 3]]

        Output: [2, 7, 14, 8]

        Explanation:
            The binary representation of the elements in the array are:
                1 = 0001
                3 = 0011
                4 = 0100
                8 = 1000
                The XOR values for queries are:
                [0, 1] = 1 xor 3 = 2
                [1, 2] = 3 xor 4 = 7
                [0, 3] = 1 xor 3 xor 4 xor 8 = 14
                [3, 3] = 8

    Example 2:

        Input: arr = [4, 8, 2, 10], queries = [[2, 3], [1, 3], [0, 0], [0, 3]]

        Output: [8, 0, 4, 4]


    Constraints:

        1 <= arr.length, queries.length <= 3 * 10^4
        1 <= arr[i] <= 10^9
        queries[i].length == 2
        0 <= left_i <= right_i < arr.length


    Topics:

        Array
        Bit Manipulation
        Prefix Sum


    Courses:

        Daily: 2024/09/13

"""


def Brt01_QursItr_XorSum_Prt(Arr, Qurs):

    print(f"\tArray: {Arr}")
    print(f"\tQueries: {Qurs}")
    print()

    print("\t\tBinary array:")
    for nm in Arr:
        print(f"\t\t\t{nm} = {bin(nm)[2:]}")

    for qr in Qurs:

        print(Arr[qr[0]:qr[1] + 1])


if __name__ == "__main__":

    InputLst = [[[1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]],
                [[4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Arr = case[0]
        Qurs = case[1]

        print(f"\tArray: {Arr}")
        print(f"\tQueries: {Qurs}")
        print()

        print("\t\tBinary array:")
        for nm in Arr:
            print(f"\t\t\t{nm} = {bin(nm)[2:]}")
        print()

        xrAr = []

        print("\t\tQueries arrays:")
        for qr in Qurs:
            lf, rg = qr[0], qr[1] + 1
            crAr = Arr[lf:rg]

            crNm = crAr[0]
            for nm in crAr[1:]:
                crNm ^= nm

            xrAr.append(crAr)

            print(f"\t\t\t{qr}: {crAr} = {crNm}")
        print()

        print(f"\tXOR Array: {xrAr}")

        print("\n")
