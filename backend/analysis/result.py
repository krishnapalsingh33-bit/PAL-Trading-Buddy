from dataclasses import dataclass, field


@dataclass
class AnalysisResult:

    status: str

    confidence: int

    reasons: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    data: dict = field(default_factory=dict)