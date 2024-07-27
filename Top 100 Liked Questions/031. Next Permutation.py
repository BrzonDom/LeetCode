"""
31. Next Permutation

https://leetcode.com/problems/next-permutation/description/

    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1, 2, 3], the following are all the permutations of arr: [1, 2, 3], [1, 3, 2], [2, 1, 3],
    [2, 3, 1], [3, 1, 2], [3, 2, 1].
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
    More formally, if all the permutations of the array are sorted in one container according to their lexicographical
    order, then the next permutation of that array is the permutation that follows it in the sorted container. If such
    arrangement is not possible, the array must be rearranged as the lowest possible order
    (i.e., sorted in ascending order).

        - For example, the next permutation of arr = [1, 2, 3] is [1, 3, 2].
        - Similarly, the next permutation of arr = [2, 3, 1] is [3, 1, 2].
        - While the next permutation of arr = [3, 2, 1] is [1, 2, 3] because [3, 2, 1] does not have a lexicographical
          larger rearrangement.

    Given an array of integers nums, find the next permutation of nums.

    The replacement must be in place and use only constant extra memory.

    Example 1:

        Input: nums = [1, 2, 3]
        Output: [1, 3, 2]

    Example 2:

        Input: nums = [3, 2, 1]
        Output: [1, 2, 3]

    Example 3:

        Input: nums = [1, 1, 5]
        Output: [1, 5, 1]


    Constraints:

        1 <= nums.length <= 100
        0 <= nums[i] <= 100

"""


from itertools import permutations


InputLst = [[1, 2, 3], [3, 2, 1], [1, 1, 5]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt+1}.Case\n")

    prmIn = case

    print(f"\tInput permutation: {prmIn}")
    print()

    PrmsLst = list(permutations(prmIn, 3))

    print(f"\t\t\tAll unsorted unset permutations:")
    for pCnt, prm in enumerate(PrmsLst):
        print(f"\t\t\t\t{pCnt+1}. {prm}")
    print()

    PrmsLst = list(set(PrmsLst))

    print(f"\t\t\tAll unsorted set permutations:")
    for pCnt, prm in enumerate(PrmsLst):
        print(f"\t\t\t\t{pCnt+1}. {prm}")
    print()

    PrmsLst = sorted(PrmsLst)
    nxtPrms = {}

    print(f"\t\tAll sorted set permutations:")
    for pCnt, prm in enumerate(PrmsLst):
        print(f"\t\t\t{pCnt+1}. {prm}")

        nxtPrms[str(prm)] = pCnt + 1
    nxtPrms[str(PrmsLst[-1])] = 0

    print("\n")
