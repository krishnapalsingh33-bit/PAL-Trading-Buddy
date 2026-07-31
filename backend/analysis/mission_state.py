from dataclasses import dataclass, field


@dataclass
class MissionState:

    target: str

    stage: str

    completed: bool = False

    next_step: str = ""

    evidence: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)