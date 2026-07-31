from enum import Enum


class LiquidityStatus(Enum):

    WAITING = "WAITING"

    TOUCHED = "TOUCHED"

    MANIPULATION = "MANIPULATION"

    CISD = "CISD"

    EXECUTED = "EXECUTED"

    ARCHIVED = "ARCHIVED"

    INVALID = "INVALID"