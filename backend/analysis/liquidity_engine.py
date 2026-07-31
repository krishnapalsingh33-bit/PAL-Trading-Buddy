from analysis.objective_detector import ObjectiveDetector
from analysis.story_selector import StorySelector

from models.liquidity_analysis import LiquidityAnalysis
from models.structure_analysis import StructureAnalysis
from models.swing_analysis import SwingAnalysis


class LiquidityEngine:

    def __init__(self):

        self.detector = ObjectiveDetector()
        self.selector = StorySelector()

    def analyze(

        self,

        structure: StructureAnalysis,

        swings: SwingAnalysis,

        latest_price: float

    ) -> LiquidityAnalysis:

        analysis = LiquidityAnalysis(

            timeframe=swings.timeframe

        )

        objectives = self.detector.detect(

            swings=swings,

            structure=structure,

            timeframe=swings.timeframe,

            latest_price=latest_price

        )

        for objective in objectives:

            if objective.side == "BUY":

                analysis.remaining_buy.append(

                    objective

                )

            else:

                analysis.remaining_sell.append(

                    objective

                )

        analysis.total_remaining = len(objectives)

        analysis = self.selector.select(

            analysis

        )

        return analysis