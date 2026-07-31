from dataclasses import dataclass


@dataclass
class ChecklistItem:
    name: str
    completed: bool
    weight: int
    reason: str


@dataclass
class ChecklistResult:
    items: list
    score: int
    completed: int
    total: int


def analyze_checklist(context, execution):

    items = [

        ChecklistItem(
            name="External Liquidity",
            completed=execution.liquidity.external_buy_side_taken
                      or execution.liquidity.external_sell_side_taken,
            weight=20,
            reason="External liquidity sweep completed."
        ),

        ChecklistItem(
            name="Manipulation",
            completed=execution.manipulation.detected,
            weight=15,
            reason="Manipulation confirmed."
        ),

        ChecklistItem(
            name="Internal Liquidity",
            completed=execution.liquidity.internal_buy_side_taken
                      or execution.liquidity.internal_sell_side_taken,
            weight=10,
            reason="Internal liquidity completed."
        ),

        ChecklistItem(
            name="DXY Alignment",
            completed=execution.alignment.aligned,
            weight=15,
            reason=execution.alignment.reason
        ),

        ChecklistItem(
            name="CISD",
            completed=execution.cisd.confirmed,
            weight=15,
            reason="CISD confirmed."
        ),

        ChecklistItem(
            name="Premium / Discount",
            completed=execution.premium.discount,
            weight=10,
            reason=execution.premium.reason
        ),

        ChecklistItem(
            name="HTF Bias",
            completed=context.htf_bias == "Bullish",
            weight=15,
            reason="Higher timeframe supports the trade."
        )

    ]

    score = sum(item.weight for item in items if item.completed)

    completed = sum(1 for item in items if item.completed)

    total = len(items)

    return ChecklistResult(
        items=items,
        score=score,
        completed=completed,
        total=total
    )