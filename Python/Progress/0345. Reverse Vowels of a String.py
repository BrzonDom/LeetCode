"""
345. Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/description/


    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


    Example 1:

        Input: s = "IceCreAm"

        Output: "AceCreIm"

        Explanation:
            The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

    Example 2:

        Input: s = "leetcode"

        Output: "leotcede"


    Constraints:

        1 <= s.length <= 3 * 10^5
        s consist of printable ASCII characters.


    Topics:

        Two Pointers
        String


    Courses:

        LeetCode 75

"""


import time


def Slt01_WhlLp_TwPntrMtd_Prt(Srt):

    ln_srt = len(Srt)
    srt_lst = list(Srt)

    print(f"\tString: {Srt}")
    print(f"\t\tLength: {ln_srt}")
    print()

    vwls = set("aeiouAEIOU")
    vwl_cnt = 1

    print("\t\tVowels in the string:")
    for idx, crc in enumerate(Srt):

        if crc in vwls:
            print(f"\t\t\t{vwl_cnt}. Str[{idx}] = {crc}")

            vwl_cnt += 1
    print()

    lft = 0
    rgt = ln_srt - 1

    print("\t\tVowel swaps:")
    while lft < rgt:

        if srt_lst[lft] not in vwls:
            lft += 1

        elif srt_lst[rgt] not in vwls:
            rgt -= 1

        else:
            print(f"\t\t\t{srt_lst[lft]} <-> {srt_lst[rgt]}")

            srt_lst[lft], srt_lst[rgt] = srt_lst[rgt], srt_lst[lft]

            lft += 1
            rgt -= 1
    print()

    srt_swp = "".join(srt_lst)

    print(f"\tSwapped string: {srt_swp}")

    return srt_swp


if __name__ == "__main__":

    StartTime = time.time()

    InputLst = ["IceCreAm",
                "leetcode"]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        # Slt01_WhlLp_TwPntrMtd_Prt(case)

        Srt = case
        ln_srt = len(Srt)

        print(f"\tString: {case}")
        print(f"\t\tLength: {ln_srt}")
        print()

        vwls = set("aeiouAEIOU")
        vwl_cnt = 1

        print("\t\tVowels in the string:")
        for idx, crc in enumerate(Srt):

            if crc in vwls:
                print(f"\t\t\t{vwl_cnt}. Str[{idx}] = {crc}")

                vwl_cnt += 1

        lft = 0
        rgt = ln_srt - 1

        while lft < rgt:

            print(Srt[lft])

            lft += 1
        print()

        lft = 0
        rgt = ln_srt - 1

        while lft < rgt:

            print(Srt[rgt])

            rgt -= 1

        print("\n")

    EndTime = time.time()

    print(f"Time: {(EndTime - StartTime) * 1000} milliseconds", end="")