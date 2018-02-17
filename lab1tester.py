"""
Lab #1 Test,
CSC148 Lab #1, Winter 2018.
"""

from lab1 import RaceRegistery
if __name__ == "__main__":
    race_1 = RaceRegistery()
    race_1.add_runner('gerhard@mail.utoronto.ca', 3)
    race_1.add_runner('tom@mail.utoronto.ca', 2)
    race_1.add_runner('toni@mail.utoronto.ca', 1)
    race_1.add_runner('margot@mail.utoronto.ca', 2)
    race_1.add_runner('gerhard@mail.utoronto.ca', 2)
    print(race_1)
    print(race_1.runners_in_speed_category(2))
