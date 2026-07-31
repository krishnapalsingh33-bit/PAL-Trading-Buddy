from enum import Enum


class Event(str, Enum):

    EXTERNAL_LIQUIDITY = "external_liquidity"

    INTERNAL_LIQUIDITY = "internal_liquidity"

    FVG_CREATED = "fvg_created"

    MANIPULATION = "manipulation"

    DISPLACEMENT = "displacement"

    CISD = "cisd"

    TARGET_REACHED = "target_reached"

    NEW_STORY = "new_story"