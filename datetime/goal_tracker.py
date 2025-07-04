import calendar
from datetime import date
from typing import Tuple

"""
Sample text if on-track:
Congratulations! You are on track with your steps goal. The target for 2023-01-12 is 164,383 steps and you are 11 ahead.

Sample text if not on track:
You have some catching up to do! The target for 2023-09-30 is 27,300 pages read and you are 2 behind.
"""


def goal_tracker(desc: str, annual_target: int, current_score: int, score_date: Tuple[int, int, int]):
     """Return a string determining whether a goal is on track
     by calculating the current target and comparing it with the current achievement.
     The function assumes the goal is to be achieved in a calendar year. Think New Year's Resolution :)
     """
     if (
             not isinstance(score_date, Tuple) or
             len(score_date) != 3 or
             not (isinstance(score_date[0], int), isinstance(score_date[1], int), isinstance(score_date[2], int))
     ):
         raise TypeError

     score_date = date(score_date[0], score_date[1], score_date[2])

     days_in_year = 365
     if (score_date.year % 4 == 0 and score_date.year % 100 != 0) or (score_date.year % 400 == 0):
         days_in_year += 1

     daily_target = float(annual_target / days_in_year)
     where_it_should_be = int(daily_target * ((score_date - date(score_date.year, 1, 1)).days + 1))

     if where_it_should_be <= current_score:
         return f"Congratulations! You are on track with your {desc} goal. The target for {score_date} is {where_it_should_be:,} {desc} and you are {current_score - where_it_should_be} ahead."

     return f"You have some catching up to do! The target for {score_date} is {where_it_should_be:,} {desc} and you are {where_it_should_be - current_score} behind."


if __name__ == "__main__":
    print(goal_tracker("steps", 5000000, 164394, (2023, 1, 12)))
    print(goal_tracker("healthy snacks", 722, 119, (2000, 2, 29)))
    print(goal_tracker("days of code", 365, 77, (2021, 3, 18)))
    print(goal_tracker("pages read", 36500, 27298, (2023, 9, 30)))
    print(goal_tracker("minutes walked", (30 * 365), 2500, (2021, 3, 30)))
    print(goal_tracker("pybites completed", 5000, 0, (2021, 1, 3)))
    print(goal_tracker("leaps", 365, 31, (2000, 2, 1)))
    print(goal_tracker("jumps", 365, 31, (2023, 2, 1)))