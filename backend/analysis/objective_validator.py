from models.liquidity_level import LiquidityLevel
from models.swing_analysis import SwingAnalysis
from models.structure_analysis import StructureAnalysis


class ObjectiveValidator:

    def validate(

        self,

        objective: LiquidityLevel,

        swings: SwingAnalysis,

        structure: StructureAnalysis

    ) -> bool:

        # ----------------------------------
        # Unknown Structure
        # ----------------------------------

        if structure.trend == "UNKNOWN":

            return False

        # ----------------------------------
        # Bullish Story
        # ----------------------------------

        if structure.trend == "BULLISH":

            if objective.side != "BUY":

                return False

        # ----------------------------------
        # Bearish Story
        # ----------------------------------

        elif structure.trend == "BEARISH":

            if objective.side != "SELL":

                return False

        # ----------------------------------
        # Transition
        # ----------------------------------

        elif structure.trend == "TRANSITION":

            return True

        return True