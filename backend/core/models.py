from dataclasses import dataclass


# ==========================
# Context
# ==========================

@dataclass
class ContextData:
    htf_bias: str
    market_structure: str
    order_flow: str
    imbalance: str
    liquidity: str


# ==========================
# Liquidity
# ==========================

@dataclass
class LiquidityData:
    external_buy_side_taken: bool
    external_sell_side_taken: bool

    internal_buy_side_taken: bool
    internal_sell_side_taken: bool

    current_external_side: str
    current_internal_side: str

    sweep_count: int


# ==========================
# Manipulation
# ==========================

@dataclass
class ManipulationData:
    detected: bool
    manipulation_count: int

    first_manipulation: bool
    second_manipulation: bool

    direction: str
    quality: str


# ==========================
# CISD
# ==========================

@dataclass
class CISDData:
    confirmed: bool

    timeframe: str

    candle_count: int

    direction: str

    displacement: bool

    imbalance_created: bool

    quality: str


# ==========================
# Alignment
# ==========================

@dataclass
class AlignmentData:
    aligned: bool

    dxy_bias: str

    gbpusd_bias: str

    inverse_correlation: bool

    confidence: int

    reason: str


# ==========================
# Premium / Discount
# ==========================

@dataclass
class PremiumData:
    location: str

    premium: bool

    discount: bool

    equilibrium: bool

    confidence: int

    reason: str


# ==========================
# Filters
# ==========================

@dataclass
class FilterData:
    high_impact_news: bool
    london_session: bool
    new_york_session: bool


# ==========================
# Execution Result
# ==========================

@dataclass
class ExecutionResult:
    liquidity: LiquidityData
    manipulation: ManipulationData
    cisd: CISDData
    alignment: AlignmentData
    premium: PremiumData


# ==========================
# Decision
# ==========================

@dataclass
class DecisionData:
    grade: str
    confidence: int
    direction: str
    reason: str


# ==========================
# PAL CORE
# ==========================

@dataclass
class PalCoreData:
    context: ContextData
    execution: ExecutionResult
    filters: FilterData
    decision: DecisionData