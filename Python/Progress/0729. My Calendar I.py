"""
729. My Calendar I

https://leetcode.com/problems/my-calendar-i/description/


    You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause
    a double booking.

    A double booking happens when two events have some non-empty intersection (i.e., some moment is common to
    both events.).

    The event can be represented as a pair of integers start and end that represents a booking on the half-open
    interval [start, end), the range of real numbers x such that start <= x < end.

    Implement the MyCalendar class:

        - MyCalendar() Initializes the calendar object.
        - boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without
          causing a double booking. Otherwise, return false and do not add the event to the calendar.


    Example 1:

        Input:
            ["MyCalendar", "book", "book", "book"]
            [[], [10, 20], [15, 25], [20, 30]]

        Output:
            [null, true, false, true]

        Explanation:
            MyCalendar myCalendar = new MyCalendar();
            myCalendar.book(10, 20); // return True
            myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked
            by another event.
            myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time
            less than 20, but not including 20.


    Constraints:

        0 <= start < end <= 10^9
        At most 1000 calls will be made to book.


    Topics:

        Array
        Binary Search
        Design
        Segment Tree
        Ordered Set


    Courses:

        Daily: 2024/09/26

"""


if __name__ == "__main__":

    InputLst = [[["MyCalendar", "book", "book", "book"], [[], [10, 20], [15, 25], [20, 30]]]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        Cld_Cmds = case[0]
        Tms = case[1]

        print(f"\tCommands: {Cld_Cmds}")
        print(f"\tTimes: {Tms}")
        print()

        bk_tms = []

        print("\tBooking times:")
        for tm in Tms:
            print(f"\t\t{tm}")

            fnd_bk = True

            for bk in bk_tms:
                print(f"\t\t\t{bk}")

            if fnd_bk:
                bk_tms.append(tm)

        print("\n")
