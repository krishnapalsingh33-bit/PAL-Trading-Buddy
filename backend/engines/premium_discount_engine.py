from models.premium_discount_analysis import PremiumDiscountAnalysis
from models.structure_analysis import StructureAnalysis


class PremiumDiscountEngine:

    def analyze(
        self,
        current_price: float,
        structure: StructureAnalysis,
    ) -> PremiumDiscountAnalysis:

        analysis = PremiumDiscountAnalysis()

        analysis.range_high = structure.high

        analysis.range_low = structure.low

        analysis.current_price = current_price

        analysis.equilibrium = (
            analysis.range_high +
            analysis.range_low
        ) / 2

        if current_price > analysis.equilibrium:

            analysis.zone = "PREMIUM"

            analysis.valid_for_sells = True

        elif current_price < analysis.equilibrium:

            analysis.zone = "DISCOUNT"

            analysis.valid_for_buys = True

        else:

            analysis.zone = "EQUILIBRIUM"

        return analysis