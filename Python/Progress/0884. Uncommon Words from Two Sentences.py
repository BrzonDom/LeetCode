"""
884. Uncommon Words from Two Sentences

https://leetcode.com/problems/uncommon-words-from-two-sentences/description/


    A sentence is a string of single-space separated words where each word consists only of lowercase letters.

    A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

    Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.


    Example 1:

        Input: s1 = "this apple is sweet", s2 = "this apple is sour"

        Output: ["sweet", "sour"]

        Explanation:
            The word "sweet" appears only in s1, while the word "sour" appears only in s2.


    Example 2:

        Input: s1 = "apple apple", s2 = "banana"

        Output: ["banana"]


    Constraints:

        1 <= s1.length, s2.length <= 200
        s1 and s2 consist of lowercase English letters and spaces.
        s1 and s2 do not have leading or trailing spaces.
        All the words in s1 and s2 are separated by a single space.


    Topics:

        Hash Table
        String
        Counting


    Course:

        Daily: 2024/09/17

"""


def Brt01_TwWrdCmpItr_Prt(Str1, Str2):

    print(f"\t1. String: {Str1}")
    print(f"\t2. String: {Str2}")
    print()

    wrd1 = Str1.split()
    wrd2 = Str2.split()

    print(f"\t1. Words: {wrd1}")
    print(f"\t2. Words: {wrd2}")
    print()

    unqWrd = []

    print("\t\t1. Unique words:")
    for wd in wrd1:
        if wrd1.count(wd) < 2:

            if wd not in wrd2:
                print(f"\t\t\t{wd}")

                unqWrd.append(wd)
    print()

    print("\t\t2. Unique words:")
    for wd in wrd2:
        if wrd2.count(wd) < 2:

            if wd not in wrd1:
                print(f"\t\t\t{wd}")

                unqWrd.append(wd)
    print()

    print(f"\tAll unique words: {unqWrd}")

    return unqWrd


def Slt01_WrdDctItr_Prt(Str1, Str2):

    print(f"\t1. String: {Str1}")
    print(f"\t2. String: {Str2}")
    print()

    wrd1 = Str1.split()
    wrd2 = Str2.split()

    print(f"\t1. Words: {wrd1}")
    print(f"\t2. Words: {wrd2}")
    print()

    cntDct = {}

    for wd in wrd1 + wrd2:

        if wd not in cntDct:
            cntDct[wd] = 1

        else:
            cntDct[wd] += 1

    print("\t\tWords count:")
    for wd, nm in cntDct.items():
        print(f"\t\t\t{wd} : {nm}")


if __name__ == "__main__":

    InputLst = [["this apple is sweet", "this apple is sour"],
                ["apple apple", "banana"]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        # Brt01_TwWrdCmpItr_Prt(case[0], case[1])

        Str1 = case[0]
        Str2 = case[1]

        print(f"\t1. String: {Str1}")
        print(f"\t2. String: {Str2}")
        print()

        wrd1 = Str1.split()
        wrd2 = Str2.split()

        print(f"\t1. Words: {wrd1}")
        print(f"\t2. Words: {wrd2}")
        print()

        cntDct = {}

        for wd in wrd1 + wrd2:

            if wd not in cntDct:
                cntDct[wd] = 1

            else:
                cntDct[wd] += 1

        unqWrds = []

        print("\t\tWords count:")
        for wd, nm in cntDct.items():
            print(f"\t\t\t{wd} : {nm}")

            if nm == 1:
                unqWrds.append(wd)
        print()

        print(f"\tAll unique words: {unqWrds}")

        print("\n")
