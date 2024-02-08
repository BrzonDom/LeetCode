"""
383. Ransom Note

https://leetcode.com/problems/ransom-note/description/

    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

    Example 1:

        Input: ransomNote = "a", magazine = "b"
        Output: false

    Example 2:

        Input: ransomNote = "aa", magazine = "ab"
        Output: false

    Example 3:

        Input: ransomNote = "aa", magazine = "aab"
        Output: true

    Constraints:

        1 <= ransomNote.length, magazine.length <= 105
        ransomNote and magazine consist of lowercase English letters.

"""

def noteComplt_Sol(Note, Magazine):

    Note_visit = ""

    for char in Note:
        if char not in Note_visit:

            if Note.count(char) > Magazine.count(char):
                return False
            Note_visit += char

    return True


def noteComplt_Prt(Note, Magazine):

    Note_visit = []

    print(f"\tNote:      {Note}")
    print(f"\tMagazine:  {Magaz}")
    print()

    complt = True

    for char in Note:
        if char not in Note_visit:
            Note_visit.append(char)
            print(f"\t\t{char} : {Note.count(char)} / {Magaz.count(char)}")
            if Note.count(char) > Magaz.count(char):
                print(f"\t\t\tMissing '{char}' letter")
                complt = False

    print()

    return complt


Input_charLst = [["a", "b"],
                 ["aa", "ab"],
                 ["aa", "aab"]]


print("Test code:\n")

Note = "aabcdaehe"
Magaz = "abbcadeeaedfea"

print(f"\tNote:      {Note}")
print(f"\tMagazine:  {Magaz}")
print()

Note_dic = {}
Magz_dic = {}

MissChar_Lst = []


for char in Note:
    if char not in Note_dic:
        Note_dic[char] = Note.count(char)
        Magz_dic[char] = Magaz.count(char)

        if Note.count(char) < Magaz.count(char):
            MissChar_Lst.append(char)


print(f"\tNote dictionary:   {Note_dic}")
print(f"\tMagaz dictionary:  {Magz_dic}")

for key in Note_dic:
    print(f"\t\t{key} : {Note_dic[key]} / {Magz_dic[key]}")
    if not Magz_dic[key]:
        print(f"\t\t\tMissing {key} letter !")
print()

print("Driver solution:\n")

for charLst in Input_charLst:

    Note = charLst[0]
    Magaz = charLst[1]

    print(f"\tNote:      {Note}")
    print(f"\tMagazine:  {Magaz}")
    print()

    Note_visit = []

    for char in Note:
        if char not in Note_visit:
            Note_visit.append(char)
            print(f"\t\t{char} : {Note.count(char)} / {Magaz.count(char)}")
            if Note.count(char) > Magaz.count(char):
                print(f"\t\t\tMissing '{char}' letter")
    print("\n")

print("Function solution:\n")

for charLst in Input_charLst:

    Note = charLst[0]
    Magaz = charLst[1]

    noteComplt_Prt(Note, Magaz)
    print(f"\tCompleted: {noteComplt_Sol(Note, Magaz)}\n\n")

