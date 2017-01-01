#!/usr/bin/env python
"""Print out a text calendar for the given year"""

import os 
import sys
import calendar


FIRSTWEEKDAY = 6


def calabazas(year):
    """Print out a calendar, with one day per row"""
    BREAK_AFTER_WEEKDAY = 6 # add a newline after this weekday

    c = calendar.Calendar()
    tc = calendar.TextCalendar(firstweekday=FIRSTWEEKDAY)
    for month in range(1, 12+1):
        print()
        tc.prmonth(year, month)
        print()
        for day, weekday in c.itermonthdays2(year, month):
            if day == 0:
                continue

            print("{:2} {} {}: ".format(day, 
                                      calendar.month_abbr[month], 
                                      calendar.day_abbr[weekday]))
            if weekday == BREAK_AFTER_WEEKDAY:
                print()
    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="print out a calendar")
    parser.add_argument('year', metavar='YEAR', type=int, help='the calendar year')
    args = parser.parse_args()

    calabazas(args.year) 
