from core.models import ContextData


def analyze_context():

    context = ContextData(
        htf_bias="Bullish",
        market_structure="Bullish",
        order_flow="Bullish",
        imbalance="Holding",
        liquidity="Buy Side Taken"
    )

    return context