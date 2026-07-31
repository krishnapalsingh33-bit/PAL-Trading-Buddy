from dataclasses import dataclass


@dataclass
class StoryLayer:

    timeframe: str = ""

    direction: str = "NONE"

    objective: str = ""

    valid: bool = False

    description: str = ""