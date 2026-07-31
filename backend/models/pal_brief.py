from dataclasses import dataclass, field


@dataclass
class PalBrief:

    greeting: str = ""

    session: str = ""

    mission: str = ""

    current_story: str = ""

    next_event: str = ""

    decision: str = ""

    grade: str = ""

    confidence: int = 0

    evidence: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)