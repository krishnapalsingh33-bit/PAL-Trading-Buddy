from dataclasses import dataclass


@dataclass
class TimeframeNode:

    name: str

    higher: str | None

    lower: str | None