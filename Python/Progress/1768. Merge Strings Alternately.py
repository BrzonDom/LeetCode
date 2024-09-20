"""
1768. Merge Strings Alternately

https://leetcode.com/problems/merge-strings-alternately/description/


    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with
    word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

    Return the merged string.


    Example 1:

        Input: word1 = "abc", word2 = "pqr"

        Output: "apbqcr"

        Explanation: The merged string will be merged as so:
            word1:  a   b   c
            word2:    p   q   r
            merged: a p b q c r

    Example 2:

        Input: word1 = "ab", word2 = "pqrs"

        Output: "apbqrs"

        Explanation: Notice that as word2 is longer, "rs" is appended to the end.
            word1:  a   b
            word2:    p   q   r   s
            merged: a p b q   r   s

    Example 3:

        Input: word1 = "abcd", word2 = "pq"

        Output: "apbqcd"

        Explanation: Notice that as word1 is longer, "cd" is appended to the end.
            word1:  a   b   c   d
            word2:    p   q
            merged: a p b q c   d


    Constraints:

        1 <= word1.length, word2.length <= 100
        word1 and word2 consist of lowercase English letters.


    Topics:

        Two Pointers
        String


    Courses:

        LeetCode 75

"""


def Slt01_WhlBth_AppRmn_Prt(Wrd1, Wrd2):

    print(f"\t1. Word: {Wrd1}")
    print(f"\t2. Word: {Wrd2}")


if __name__ == "__main__":

    InputLst = [["abc", "pqr"],
                ["ab", "pqrs"],
                ["abcd", "pq"]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Wrd1 = case[0]
        Wrd2 = case[1]

        print(f"\t1. Word: {Wrd1}")
        print(f"\t2. Word: {Wrd2}")
        print()

        mrg_Wrd = ""

        print("\t\tWord character pairs:")
        while Wrd1 and Wrd2:
            print(f"\t\t\t{Wrd1[0]} : {Wrd2[0]}")

            mrg_Wrd += Wrd1[0] + Wrd2[0]

            Wrd1 = Wrd1[1:]
            Wrd2 = Wrd2[1:]
        print()

        if Wrd1:
            print("\t\tRemaining 1. word:")
            print(f"\t\t\t{Wrd1}")
            print()

            mrg_Wrd += Wrd1

        elif Wrd2:
            print("\t\tRemaining 2. word:")
            print(f"\t\t\t{Wrd2}")
            print()

            mrg_Wrd += Wrd2

        print(f"\tMerged words: {mrg_Wrd}")

        print("\n")
