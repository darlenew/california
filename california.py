#!/usr/bin/env python
"""Print out a text calendar for the given year"""

import os 
import sys
import calendar


FIRSTWEEKDAY = 6
WEEKEND = (5, 6) # day-of-week indices for saturday and sunday


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
   

def calcium(year, weekends=True):
    """Print out a [YYYYMMDD] calendar, no breaks between weeks/months"""
    tc = calendar.TextCalendar()
    for month_index, month in enumerate(tc.yeardays2calendar(year, width=1), 1):
        for week in month[0]: # ?
            for day, weekday in week:
                if not day:
                    continue
                if not weekends and weekday in (WEEKEND):
                    print()
                    continue
                print(f"[{year}{month_index:02}{day:02}]")


def calzone(year):
    """Prints YYYYMMDD calendar, like calcium without weekends"""
    return calcium(year, weekends=False)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="print out a calendar")
    parser.add_argument('year', metavar='YEAR', type=int, help='the calendar year')
    parser.add_argument('style', metavar='STYLE', help='calendar style')
    args = parser.parse_args()

    style = {'calcium': calcium,
             'calabazas': calabazas,
             'calzone': calzone,
             }
    try:
        style[args.style](args.year)
    except KeyError:
        raise(f"Calendar style {args.style} not found")
