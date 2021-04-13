from enum import Enum, auto


class AutoName(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()


class ClubEnum(AutoName):
    PK = auto()
    NAME = auto()


class PlayerEnum(AutoName):
    PK = auto()
    NAME = auto()
    AGE = auto()
    NATIONALITY = auto()
    OVERALL = auto()
    POTENTIAL = auto()
    CLUB = auto()
    VALUE = auto()
    WAGE = auto()
    PREFERRED = auto()
    INTERNATIONAL_REPUTATION = auto()
    WEAK_FOOT = auto()
    SKILL_MOVES = auto()
    POSITION = auto()
    JERSEY_NUMBER = auto()
    JOINED = auto()
    LOANED_FROM = auto()
    CONTRACT_VALID_UNTIL = auto()
    HEIGHT = auto()
    WEIGHT = auto()
