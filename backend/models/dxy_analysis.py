from dataclasses import dataclass, field


@dataclass
class DXYAnalysis:

    trend: str = "UNKNOWN"

    liquidity: str = "UNKNOWN"

    manipulation: bool = False

    displacement: bool = False

    cisd: bool = False

    premium: bool = False

    discount: bool = False

    bullish_fvg: bool = False

    bearish_fvg: bool = False

    confidence: int = 0

    gbp_alignment: bool = False

    expected_gbp_direction: str = "UNKNOWN"

    confirmations: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    summary: str = ""