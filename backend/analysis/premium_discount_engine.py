from models.market_narrative import MarketNarrative
from models.premium_discount_analysis import PremiumDiscountAnalysis


class PremiumDiscountEngine:
    """
    Determines whether price is trading in Premium,
    Discount or Equilibrium within the active dealing range.
    """

    def analyze(
        self,
        narrative: MarketNarrative,
        current_price: float
    ) -> PremiumDiscountAnalysis:

        result = PremiumDiscountAnalysis()

        result.current_price = current_price

        # ----------------------------------
        # Validation
        # ----------------------------------

        if narrative.structure is None:

            result.story = "No structure."
            result.summary = result.story
            return result

        if (
            narrative.liquidity is None
            or narrative.liquidity.current_objective is None
        ):

            result.story = "No active liquidity."
            result.summary = result.story
            return result

        objective = narrative.liquidity.current_objective

        # ----------------------------------
        # Determine Dealing Range
        # ----------------------------------

        if objective.side == "BUY":

            low = narrative.structure.protected_low
            high = objective.candle

            if low is None:

                result.story = "Protected low not available."
                result.summary = result.story
                return result

        elif objective.side == "SELL":

            high = narrative.structure.protected_high
            low = objective.candle

            if high is None:

                result.story = "Protected high not available."
                result.summary = result.story
                return result

        else:

            result.story = "Unknown liquidity side."
            result.summary = result.story
            return result

        result.dealing_range_high = high
        result.dealing_range_low = low

        equilibrium = (
            high.high + low.low
        ) / 2

        result.equilibrium = equilibrium

        # ----------------------------------
        # Premium / Discount
        # ----------------------------------

        if current_price > equilibrium:

            result.premium = True

            result.story = "Price trading in Premium."

        elif current_price < equilibrium:

            result.discount = True

            result.story = "Price trading in Discount."

        else:

            result.equilibrium_zone = True

            result.story = "Price at Equilibrium."

        result.summary = (
            f"Price={current_price:.5f} | "
            f"EQ={equilibrium:.5f} | "
            f"{result.story}"
        )

        return result