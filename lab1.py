"""
CSC148 Lab #1, Winter 2018.

@author Abdullah Khokhar
"""
from typing import List, Dict


class RaceRegistery:

    """
    Represent a race registry which includes details about the runners taking
    part of the race and organizes them in respect to their speed category and
    e-mail.
    The speed categories are:
        - 1: if speed less than 20
        - 2: if speed less than 30
        - 3: if speed less than 40
        - 4: if speed greater than or equal to 40
    """
    email_to_speed: Dict[str, int]
    speed_to_emails: Dict[int, List[str]]

    def __init__(self) -> None:
        """
        Initialize a new registery for a race.

        >>> registery_1 = RaceRegistery()
        >>> registery_1.email_to_speed
        {}
        >>> registery_1.speed_to_emails
        {}
        """

        self.email_to_speed = {}
        self.speed_to_emails = {}
        self.category = {1: 'less than 20 minutes', 2: 'less than 30 minutes',
                         3: 'less than 40 minutes', 4: 'greater than or equal '
                                                       'to 40 minutes'}

    def __eq__(self, other: "RaceRegistery") -> bool:
        """
        Return True if self has the same amount of contestants as other.

        >>> registery = RaceRegistery()
        >>> registery.add_runner('tom@hotmail.com', 1)
        >>> registery.add_runner('bob@hotmail.com', 1)
        >>> registery_2 = RaceRegistery()
        >>> registery_2.add_runner('becky@hotmail.com', 1)
        >>> registery_2.add_runner('linda@hotmail.com', 3)

        >>> registery == registery_2
        True
        """
        return len(self.email_to_speed) == len(other.email_to_speed)

    def __str__(self) -> str:
        """
        Return a string representation of self.

        >>> race_1 = RaceRegistery()
        >>> race_1.add_runner('tom@hotmail.com', 1)
        >>> race_1.add_runner('bob@hotmail.com', 2)
        >>> race_1.add_runner('danny@hotmail.com', 4)

        >>> print(race_1)
        The following 3 are contestants of the race:
        - tom@hotmail.com: less than 20 minutes
        - bob@hotmail.com: less than 30 minutes
        - danny@hotmail.com: greater than or equal to 40 minutes

        >>> race_2 = RaceRegistery()
        >>> print(race_2)
        There are no contestants part of this race.
        """
        str1 = ''
        str2 = ''

        if len(self.email_to_speed) == 0:
            return 'There are no contestants part of this race.'

        for e_mails in self.email_to_speed:
            str2 += '\n- {}: {}'.\
                format(e_mails, self.category[self.email_to_speed[e_mails]])
            str1 = 'The following {} are contestants of the race:'.\
                format(len(self.email_to_speed))
        return str1 + str2

    def add_runner(self, e_mail: 'str', speed_category: 'int') -> None:
        """
        Update the email_to_speed dictionary by adding an email, e_mail, with
        its associated speed category, speed_category, and the speed_to_emails
        dictionary by having all emails associated with its speed_category.

        Pre-Condition: category can only be 1, 2, 3, 4.

        >>> registery_1 = RaceRegistery()
        >>> registery_1.add_runner('tom@hotmail.com', 1)
        >>> registery_1.add_runner('bob@hotmail.com', 2)
        >>> registery_1.add_runner('danny@hotmail.com', 3)
        >>> registery_1.email_to_speed
        {'tom@hotmail.com': 1, 'bob@hotmail.com': 2, 'danny@hotmail.com': 3}

        >>> registery_1.speed_to_emails
        {1: ['tom@hotmail.com'], 2: ['bob@hotmail.com'], 3: \
['danny@hotmail.com']}

        """
        self.email_to_speed[e_mail] = speed_category

        if speed_category not in self.speed_to_emails:
            self.speed_to_emails[speed_category] = []
        self.speed_to_emails[speed_category].append(e_mail)

    def find_runner_speed(self, runner: 'str') -> str:
        """
        Return the speed category of runner.

        >>> race_1 = RaceRegistery()
        >>> race_1.add_runner('abd@hotmail.com', 2)
        >>> race_1.add_runner('mat@hotmail.com', 1)

        >>> race_1.find_runner_speed('abd@hotmail.com')
        'The speed category of abd@hotmail.com is: 2'
        """
        if runner in self.email_to_speed:
            return 'The speed category of {} is: {}'\
                .format(runner, self.email_to_speed[runner])
        else:
            return 'This runner is not part of this race registry'

    def runners_in_speed_category(self, speed_category: 'int') -> str:
        """
        Return a list of contestants with the speed category speed_category,
        arranged in alphabetical order.

        >>> race = RaceRegistery()
        >>> race.add_runner('abd@hotmail.com', 2)
        >>> race.add_runner('mat@hotmail.com', 2)
        >>> race.add_runner('holmes@hotmail.com', 2)

        >>> race.runners_in_speed_category(2)
        "The runners with speed category 2 are: ['abd@hotmail.com', 'holmes@hot\
mail.com', 'mat@hotmail.com']"

        >>> race.runners_in_speed_category(1)
        'There are no runners with this speed category'
        """

        if speed_category not in self.speed_to_emails:
            return 'There are no runners with this speed category'
        else:
            self.speed_to_emails[speed_category].sort()
            return 'The runners with speed category {} are: {}'.\
                format(speed_category, self.speed_to_emails[speed_category])


if __name__ == "__main__":
    from doctest import testmod
    testmod()
