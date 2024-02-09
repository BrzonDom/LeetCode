"""
3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

    Given a string s, find the length of the longest
    substring without repeating characters.

    Example 1:

        Input: s = "abcabcbb"
        Output: 3

        Explanation: The answer is "abc", with the length of 3.

    Example 2:

        Input: s = "bbbbb"
        Output: 1

        Explanation: The answer is "b", with the length of 1.

    Example 3:

        Input: s = "pwwkew"
        Output: 3

        Explanation: The answer is "wke", with the length of 3.
            Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Constraints:

        0 <= s.length <= 5 * 10⁴
        s consists of English letters, digits, symbols and spaces.
"""

Input_strLst = ["abcabcbb",
                "bbbbb",
                "pwwkew"]

print("Driver solution:\n")

for string in Input_strLst:

    print("\tString: ", string)
    print()

    subLen = 0
    maxSubLen = 0

    used = set()

    print("\t", end="\t")
    for char in string:

        if char not in used:
            print(char, end="")

            used.add(char)
            subLen += 1

        else:
            print("\n\t", end="\t")
            print(char, end="")

            if subLen > maxSubLen:
                maxSubLen = subLen

            subLen = 1
            used.clear()
            used.add(char)

    if subLen > maxSubLen:
        maxSubLen = subLen

    print("\n\n\tMax len of substring: ", maxSubLen)
    print("\n")








