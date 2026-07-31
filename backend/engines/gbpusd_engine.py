from engines.structure_engine import StructureEngine
from engines.liquidity_engine import LiquidityEngine
from engines.manipulation_engine import ManipulationEngine
from engines.displacement_engine import DisplacementEngine
from engines.delivery_engine import DeliveryEngine
from engines.cisd_engine import CISDEngine

from models.gbpusd_analysis import GBPUSDAnalysis


class GBPUSDEngine:

    def __init__(self):

        self.structure_engine = StructureEngine()

        self.liquidity_engine = LiquidityEngine()

        self.manipulation_engine = ManipulationEngine()

        self.displacement_engine = DisplacementEngine()

        self.delivery_engine = DeliveryEngine()

        self.cisd_engine = CISDEngine()

    def analyze(
        self,
        candles,
        timeframe: str,
    ) -> GBPUSDAnalysis:

        analysis = GBPUSDAnalysis(
            timeframe=timeframe
        )

        # ----------------------------
        # Structure
        # ----------------------------

        analysis.structure = (
            self.structure_engine.analyze(
                candles,
                timeframe,
            )
        )

        # ----------------------------
        # Liquidity
        # ----------------------------

        analysis.liquidity = (
            self.liquidity_engine.analyze(
                candles,
                analysis.structure,
                timeframe,
            )
        )

        # ----------------------------
        # Manipulation
        # ----------------------------

        analysis.manipulation = (
            self.manipulation_engine.analyze(
                candles,
                analysis.liquidity,
                timeframe,
            )
        )

        # ----------------------------
        # Displacement
        # ----------------------------

       analysis.displacement = (
    self.displacement_engine.analyze(
        candles,
        analysis.manipulation,
        timeframe,
    )
)

        # ----------------------------
        # Delivery
        # ----------------------------

       analysis.delivery = (
    self.delivery_engine.analyze(
        analysis.displacement,
        timeframe,
    )
)

        # ----------------------------
        # CISD
        # ----------------------------

        analysis.cisd = (
    self.cisd_engine.analyze(
        analysis.delivery,
    )
)

        analysis.summary = (
            f"Trend: {analysis.structure.trend} | "
            f"Liquidity: {analysis.liquidity.last_sweep} | "
            f"Manipulation: {analysis.manipulation.detected} | "
            f"Displacement: {analysis.displacement.confirmed} | "
            f"Delivery: {analysis.delivery.direction} | "
            f"CISD: {analysis.cisd.confirmed}"
        )

        return analysis