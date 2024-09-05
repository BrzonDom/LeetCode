"""
125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome/description/


    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
    all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include
    letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.


    Example 1:

        Input: s = "A man, a plan, a canal: Panama"

        Output: true

        Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:

        Input: s = "race a car"

        Output: false

        Explanation: "raceacar" is not a palindrome.

    Example 3:

        Input: s = " "

        Output: true

        Explanation: s is an empty string "" after removing non-alphanumeric characters.
            Since an empty string reads the same forward and backward, it is a palindrome.


    Constraints:

        1 <= s.length <= 2 * 10^5
        s consists only of printable ASCII characters.


    Tags:

        Two Pointers
        String

"""


if __name__ == "__main__":

    InputLst = ["A man, a plan, a canal: Panama",
                "race a car",
                " "]

    print(f"\ta: {ord('a')}")
    print(f"\tz: {ord('z')}")
    print()

    print(f"\tA: {ord('A')}")
    print(f"\tZ: {ord('Z')}")
    print()

    print(f"\ta - A: {ord('a') - ord('A')}")
    print(f"\tz - Z: {ord('z') - ord('Z')}")

    print("\n")

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Org = case

        print(f"\tOriginal string: \"{Org}\"")
        print()

        for chr in Org:
            print(chr)

        print("\n")
