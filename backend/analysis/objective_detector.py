from analysis.objective_validator import ObjectiveValidator

from models.liquidity_level import LiquidityLevel
from models.swing_analysis import SwingAnalysis
from models.structure_analysis import StructureAnalysis


class ObjectiveDetector:

    def __init__(self):

        self.validator = ObjectiveValidator()

    def detect(
        self,
        swings: SwingAnalysis,
        structure: StructureAnalysis,
        timeframe: str,
        latest_price: float
    ) -> list[LiquidityLevel]:

        objectives = []

        # ----------------------------------
        # Build Candidate Objectives
        # ----------------------------------

        if timeframe in ("Weekly", "Daily"):

            if structure.external_high:

                objectives.append(
                    LiquidityLevel(
                        candle=structure.external_high,
                        side="BUY",
                        level_type="EXTERNAL",
                        timeframe=timeframe,
                        importance=100
                    )
                )

            if structure.external_low:

                objectives.append(
                    LiquidityLevel(
                        candle=structure.external_low,
                        side="SELL",
                        level_type="EXTERNAL",
                        timeframe=timeframe,
                        importance=100
                    )
                )

        else:

            for swing in swings.meaningful_highs:

                objectives.append(
                    LiquidityLevel(
                        candle=swing,
                        side="BUY",
                        level_type="INTERNAL",
                        timeframe=timeframe,
                        importance=70
                    )
                )

            for swing in swings.meaningful_lows:

                objectives.append(
                    LiquidityLevel(
                        candle=swing,
                        side="SELL",
                        level_type="INTERNAL",
                        timeframe=timeframe,
                        importance=70
                    )
                )

        # ----------------------------------
        # Validate
        # ----------------------------------

        objectives = [

            obj
            for obj in objectives
            if self.validator.validate(
                obj,
                swings,
                structure
            )

        ]

        # ----------------------------------
        # Rank by Nearest Untaken Liquidity
        # ----------------------------------

        def liquidity_price(level: LiquidityLevel):

            if level.side == "BUY":
                return level.candle.high

            return level.candle.low

        objectives.sort(

            key=lambda level: (

                abs(liquidity_price(level) - latest_price),

                0 if level.level_type == "EXTERNAL" else 1,

                -level.importance

            )

        )

        return objectives