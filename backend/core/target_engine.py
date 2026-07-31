from dataclasses import dataclass


@dataclass
class TargetData:
    target_name: str
    target_valid: bool
    target_type: str
    confidence: int
    reason: str


def analyze_target():

    return TargetData(
        target_name="Weekly Buy Side Liquidity",
        target_valid=True,
        target_type="External Liquidity",
        confidence=95,
        reason="Higher timeframe liquidity remains the objective."
    )