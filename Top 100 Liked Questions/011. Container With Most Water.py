"""
11. Container With Most Water

https://leetcode.com/problems/container-with-most-water/description/

    You are given an integer array height of length n.
    There are n vertical lines drawn such that
    the two endpoints of the i-th line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container,
    such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    Example 1:

        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49

        Explanation:
            The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
            In this case, the max area of water the container can contain is 49.


    Example 2:

        Input: height = [1,1]
        Output: 1

    Constraints:

        n == height.length
        2 <= n <= 10⁵
        0 <= height[i] <= 10⁴

"""


def comb_contVol_Prt(heights):

    print("\tHeights:", heights)
    print()

    """     maxVol ~ Maximal volume of the container    """
    maxVol = 0
    """     maxVolDim ~ Dimensions of the maximal volume of the container"""
    maxVolDim = []

    for posBs in range(len(heights)):

        """     posBs ~ Base position, 1. position of a boarder of the container     """
        """     heiBs ~ Base height, 1. height of a boarder of the container     """
        heiBs = heights[posBs]

        """     pos ~ Next position, 2. position of a boarder of the container    """
        pos = posBs

        for hei in heights[posBs + 1:]:
            pos += 1

            """     hei ~ Next border, 2. height of a boarder of the container   """
            print(f"\t\t [{heiBs}, {posBs}] [{hei}, {pos}]")

            """     min(hei, heiBs) ~ Height of the container     """
            """     pos - posBs ~ Width of the container    """
            print(f"\t\t\tCont. height / width:  {min(hei, heiBs)} / {(pos - posBs)}")

            """     vol ~ Volume of the container   
                        Volume = Height * Width     """
            vol = min(hei, heiBs) * (pos - posBs)
            print("\t\t\tCont. volume: ", vol)

            if vol >= maxVol:
                maxVol = vol
                maxVolDim = [min(hei, heiBs), pos - posBs]
        print()

    print("\tMax cont. volume:", maxVol)
    print(f"\t\tMax cont. height / width: {maxVolDim[0]} / {maxVolDim[1]}")

    # print("\n")

    return maxVol


def encl_contVol_Prt(heights):

    print("\tHeights:", heights)
    print()

    """     maxVol ~ Maximal volume of the container    """
    maxVol = 0
    """     maxVolDim ~ Dimensions of the maximal volume of the container"""
    maxVolDim = []

    """     posL ~ Position of the Left boarder     """
    posL = 0
    """     posR ~ Position of the Right boarder    """
    posR = len(heights) - 1

    while posL != posR:

        """     heiL ~ Height of the Left boarder   """
        heiL = heights[posL]
        """     heiR ~ Height of the Right boarder  """
        heiR = heights[posR]

        print(f"\t\tContainer boarders:  [{heiL}, {posL}] [{heiR}, {posR}]")

        """     height ~ Height of the container, height = min(heiL, heiR)  """
        height = min(heiL, heiR)
        """     width ~ Width of the container, width = posR - posL     """
        width = posR - posL
        """     volume ~ Volume of the container, volume = height * width   """
        volume = height * width

        print(f"\t\tContainer volume: {volume}")
        print(f"\t\t\tContainer width:  {width}")
        print(f"\t\t\tContainer height: {height}")
        print()

        if volume > maxVol:
            maxVol = volume
            maxVolDim = [height, width]

        if heiL >= heiR:
            """     If height of the Left boarder is bigger
                        shift position of the Right boarder to the left     """
            posR -= 1
        else:
            """     If height of the Right boarder is bigger
                        shift position of the Left boarder to the right     """
            posL += 1

    print()
    print("\tMax cont. volume:", maxVol)
    print(f"\t\tMax cont. height / width: {maxVolDim[0]} / {maxVolDim[1]}")

    # print("\n")

    return maxVol


Input_heightLst = [[1, 8, 6, 2, 5, 4, 8, 3, 7],
                   [1, 1]]

print("Driver print:\n")

for heights in Input_heightLst:
    print("\tHeights:", heights)
    print()

    """     borDim ~ Border dimensions  """
    borDim = []

    print("\t\t[height, position]")
    for pos, hei in enumerate(heights):
        borDim.append([hei, pos])

    print("\t\t", borDim)
    print("\n")


print()
print("1. Driver solution via combinations:\n")

for heights in Input_heightLst:
    print("\tHeights:", heights)
    print()

    """     maxVol ~ Maximal volume of the container    """
    maxVol = 0
    """     maxVolDim ~ Dimensions of the maximal volume of the container"""
    maxVolDim = []

    for posBs in range(len(heights)):

        """     posBs ~ Base position, 1. position of a boarder of the container     """
        """     heiBs ~ Base height, 1. height of a boarder of the container     """
        heiBs = heights[posBs]

        """     pos ~ Next position, 2. position of a boarder of the container    """
        pos = posBs

        for hei in heights[posBs + 1:]:
            pos += 1

            """     hei ~ Next border, 2. height of a boarder of the container   """
            print(f"\t\t [{heiBs}, {posBs}] [{hei}, {pos}]")

            """     min(hei, heiBs) ~ Height of the container     """
            """     pos - posBs ~ Width of the container    """
            print(f"\t\t\tCont. height / width:  {min(hei, heiBs)} / {(pos - posBs)}")

            """     vol ~ Volume of the container
                        Volume = Height * Width     """
            vol = min(hei, heiBs) * (pos - posBs)
            print("\t\t\tCont. volume: ", vol)

            if vol >= maxVol:
                maxVol = vol
                maxVolDim = [min(hei, heiBs), pos - posBs]
        print()

    print("\tMax cont. volume:", maxVol)
    print(f"\t\tMax cont. height / width: {maxVolDim[0]} / {maxVolDim[1]}")

    print("\n")


print()
print("1. Function solution via combinations:\n")

for heights in Input_heightLst:

    comb_contVol_Prt(heights)


print()
print("2. Driver solution via enclosing:\n")

for heights in Input_heightLst:

    print("\tHeights:", heights)
    print()

    """     maxVol ~ Maximal volume of the container    """
    maxVol = 0
    """     maxVolDim ~ Dimensions of the maximal volume of the container"""
    maxVolDim = []

    """     posL ~ Position of the Left boarder     """
    posL = 0
    """     posR ~ Position of the Right boarder    """
    posR = len(heights) - 1

    while posL != posR:

        """     heiL ~ Height of the Left boarder   """
        heiL = heights[posL]
        """     heiR ~ Height of the Right boarder  """
        heiR = heights[posR]

        print(f"\t\tContainer boarders:  [{heiL}, {posL}] [{heiR}, {posR}]")

        """     height ~ Height of the container, height = min(heiL, heiR)  """
        height = min(heiL, heiR)
        """     width ~ Width of the container, width = posR - posL     """
        width = posR - posL
        """     volume ~ Volume of the container, volume = height * width   """
        volume = height * width

        print(f"\t\tContainer volume: {volume}")
        print(f"\t\t\tContainer width:  {width}")
        print(f"\t\t\tContainer height: {height}")
        print()

        if volume > maxVol:
            maxVol = volume
            maxVolDim = [height, width]

        if heiL >= heiR:
            """     If height of the Left boarder is bigger
                        shift position of the Right boarder to the left     """
            posR -= 1
        else:
            """     If height of the Right boarder is bigger
                        shift position of the Left boarder to the right     """
            posL += 1

    print()
    print("\tMax cont. volume:", maxVol)
    print(f"\t\tMax cont. height / width: {maxVolDim[0]} / {maxVolDim[1]}")

    print("\n")

print()
print("2. Function solution via enclosing:\n")

for heights in Input_heightLst:
    maxVol = encl_contVol_Prt(heights)
    print()

    print("\t\tMax cont. volume:", maxVol)
    print("\n")