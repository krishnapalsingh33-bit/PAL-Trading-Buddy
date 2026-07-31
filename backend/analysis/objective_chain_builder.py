from models.objective_chain import ObjectiveChain
from models.liquidity_level import LiquidityLevel

from models.structure_analysis import StructureAnalysis
from models.swing_analysis import SwingAnalysis


class ObjectiveChainBuilder:

    def build(

        self,

        structure: StructureAnalysis,

        swings: SwingAnalysis,

        side: str

    ) -> ObjectiveChain:

        chain = ObjectiveChain()

        # ------------------------------------
        # External Destination
        # ------------------------------------

        if side == "BUY":

            if structure.external_high:

                chain.external = LiquidityLevel(

                    candle=structure.external_high,

                    side="BUY",

                    level_type="EXTERNAL",

                    timeframe=structure.timeframe,

                    importance=100

                )

            for swing in swings.swing_highs:

                chain.internals.append(

                    LiquidityLevel(

                        candle=swing,

                        side="BUY",

                        level_type="INTERNAL",

                        timeframe=structure.timeframe,

                        importance=50

                    )

                )

        else:

            if structure.external_low:

                chain.external = LiquidityLevel(

                    candle=structure.external_low,

                    side="SELL",

                    level_type="EXTERNAL",

                    timeframe=structure.timeframe,

                    importance=100

                )

            for swing in swings.swing_lows:

                chain.internals.append(

                    LiquidityLevel(

                        candle=swing,

                        side="SELL",

                        level_type="INTERNAL",

                        timeframe=structure.timeframe,

                        importance=50

                    )

                )

        # ------------------------------------
        # Current Checkpoint
        # ------------------------------------

        if chain.internals:

            chain.current_internal = chain.internals[0]

        return chain