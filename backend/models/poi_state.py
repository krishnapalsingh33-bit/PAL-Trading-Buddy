from dataclasses import dataclass


@dataclass
class POIState:

    timeframe: str = ""

    inside: bool = False

    poi_type: str = ""

    description: str = ""

    confidence: int = 0