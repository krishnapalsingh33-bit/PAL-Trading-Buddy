from dataclasses import dataclass, field
from typing import Any


@dataclass
class PALReport:
    """
    Final response returned by the PAL API.
    """

    # ==========================================================
    # Basic Information
    # ==========================================================

    symbol: str = ""
    timestamp: str = ""
    success: bool = True

    # ==========================================================
    # Engine Outputs
    # ==========================================================

    market_health: dict[str, Any] = field(default_factory=dict)

    news: dict[str, Any] = field(default_factory=dict)

    dxy: dict[str, Any] = field(default_factory=dict)

    pal: dict[str, Any] = field(default_factory=dict)

    execution: dict[str, Any] = field(default_factory=dict)

    ai_commentary: dict[str, Any] = field(default_factory=dict)

    # ==========================================================
    # Dashboard Summary
    # ==========================================================

    summary: dict[str, Any] = field(default_factory=dict)