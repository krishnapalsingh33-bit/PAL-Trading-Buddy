from models.market_context import MarketContext
from models.timeframe_context import TimeframeContext
from models.market_narrative import MarketNarrative

from analysis.swing_detector import SwingDetector
from analysis.meaningful_swing_filter import MeaningfulSwingFilter
from analysis.structure_engine import StructureEngine
from analysis.liquidity_engine import LiquidityEngine
from analysis.manipulation_engine import ManipulationEngine
from analysis.displacement_engine import DisplacementEngine
from analysis.delivery_engine import DeliveryEngine
from analysis.cisd_engine import CISDEngine
from analysis.premium_discount_engine import PremiumDiscountEngine
from analysis.fvg_engine import FVGEngine
from analysis.market_state_engine import MarketStateEngine


class ContextBuilder:

    def __init__(self):

        self.swing = SwingDetector()
        self.filter = MeaningfulSwingFilter()

        self.structure = StructureEngine()
        self.liquidity = LiquidityEngine()

        self.manipulation = ManipulationEngine()
        self.displacement = DisplacementEngine()
        self.delivery = DeliveryEngine()
        self.cisd = CISDEngine()

        self.premium_discount = PremiumDiscountEngine()
        self.fvg = FVGEngine()

        self.market_state = MarketStateEngine()

    def build(self, market: MarketContext):

        context = MarketContext()

        context.symbol = market.symbol

        context.weekly = self.build_timeframe(
            market.weekly
        )

        context.daily = self.build_timeframe(
            market.daily
        )

        context.h4 = self.build_timeframe(
            market.h4
        )

        context.h1 = self.build_timeframe(
            market.h1
        )

        context.m30 = self.build_timeframe(
            market.m30
        )

        context.m15 = self.build_timeframe(
            market.m15
        )

        context.m5 = self.build_timeframe(
            market.m5
        )

        return context

    def build_timeframe(
        self,
        timeframe_data
    ):

        timeframe = timeframe_data.timeframe

        candles = timeframe_data.candles

        if len(candles) == 0:

            raise ValueError(
                f"No candles supplied for {timeframe}"
            )

        latest_price = candles[-1].close

        # ----------------------------------
        # Swing Detection
        # ----------------------------------

        swings = self.swing.detect(
            candles,
            timeframe
        )

        swings = self.filter.filter(
            swings
        )

        # ----------------------------------
        # Structure
        # ----------------------------------

        structure = self.structure.analyze(
            swings
        )

        # ----------------------------------
        # Liquidity
        # ----------------------------------

        liquidity = self.liquidity.analyze(
            structure,
            swings,
            latest_price
        )

        # ----------------------------------
        # Narrative
        # ----------------------------------

        narrative = MarketNarrative(
            structure=structure,
            liquidity=liquidity
        )

        # ----------------------------------
        # Manipulation
        # ----------------------------------

        manipulation = self.manipulation.analyze(
            candles,
            narrative
        )

        narrative.manipulation = manipulation

        # ----------------------------------
        # Displacement
        # ----------------------------------

        displacement = self.displacement.analyze(
            candles,
            narrative
        )

        narrative.displacement = displacement

        # ----------------------------------
        # Delivery
        # ----------------------------------

        delivery = self.delivery.analyze(
            candles,
            narrative,
            timeframe
        )

        narrative.delivery = delivery

        # ----------------------------------
        # CISD
        # ----------------------------------

        cisd = self.cisd.analyze(
            candles,
            narrative
        )

        narrative.cisd = cisd

        # ----------------------------------
        # Premium / Discount
        # ----------------------------------

        premium_discount = self.premium_discount.analyze(
            narrative,
            latest_price
        )

        narrative.premium_discount = premium_discount

        # ----------------------------------
        # Fair Value Gap
        # ----------------------------------

        fvg = self.fvg.analyze(
            candles,
            narrative
        )

        narrative.fvg = fvg

        # ----------------------------------
        # Market State
        # ----------------------------------

        market_state = self.market_state.build(
            liquidity,
            latest_price
        )

        # ----------------------------------
        # Return
        # ----------------------------------

        return TimeframeContext(

            timeframe=timeframe,

            swings=swings,

            structure=structure,

            liquidity=liquidity,

            manipulation=manipulation,

            displacement=displacement,

            delivery=delivery,

            cisd=cisd,

            premium_discount=premium_discount,

            fvg=fvg,

            market_state=market_state

        )