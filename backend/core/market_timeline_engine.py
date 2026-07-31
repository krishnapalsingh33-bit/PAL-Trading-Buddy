from dataclasses import dataclass


@dataclass
class TimelineStep:
    name: str
    completed: bool
    active: bool
    description: str


@dataclass
class TimelineData:
    steps: list


def analyze_market_timeline(core):

    steps = [

        TimelineStep(
            name="Asia Liquidity",
            completed=True,
            active=False,
            description="Asia range formed."
        ),

        TimelineStep(
            name="Manipulation",
            completed=True,
            active=False,
            description="Liquidity sweep completed."
        ),

        TimelineStep(
            name="Expansion",
            completed=False,
            active=True,
            description="Waiting for CISD confirmation."
        ),

        TimelineStep(
            name="Distribution",
            completed=False,
            active=False,
            description="Waiting for target delivery."
        ),

    ]

    return TimelineData(steps)