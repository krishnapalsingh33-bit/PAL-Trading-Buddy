from engines.structure_engine import StructureEngine
from engines.liquidity_engine import LiquidityEngine
from engines.manipulation_engine import ManipulationEngine
from engines.displacement_engine import DisplacementEngine
from engines.delivery_engine import DeliveryEngine
from engines.cisd_engine import CISDEngine
from engines.trend_engine import TrendEngine
from engines.story_engine import StoryEngine
from engines.trading_engine import TradingEngine
from engines.execution_engine import ExecutionEngine
from engines.pal_brain import PALBrain
from engines.report_engine import ReportEngine

from models.pal_context import PALContext


class PALAnalysisService:

    def __init__(self):

        self.structure_engine = StructureEngine()
        self.liquidity_engine = LiquidityEngine()
        self.manipulation_engine = ManipulationEngine()
        self.displacement_engine = DisplacementEngine()
        self.delivery_engine = DeliveryEngine()
        self.cisd_engine = CISDEngine()

        self.trend_engine = TrendEngine()
        self.story_engine = StoryEngine()
        self.trading_engine = TradingEngine()
        self.execution_engine = ExecutionEngine()

        self.pal_brain = PALBrain()
        self.report_engine = ReportEngine()

    def analyze(self, market_data):

        context = PALContext()

        # ======================================================
        # CORE ANALYSIS
        # ======================================================

        context.structure = self.structure_engine.analyze(
            market_data
        )

        context.liquidity = self.liquidity_engine.analyze(
            market_data,
            context.structure,
        )

        context.manipulation = self.manipulation_engine.analyze(
            market_data,
            context.liquidity,
        )

        context.displacement = self.displacement_engine.analyze(
            market_data,
            context.manipulation,
        )

        context.delivery = self.delivery_engine.analyze(
            market_data,
            context.displacement,
        )

        context.cisd = self.cisd_engine.analyze(
            market_data,
            context.delivery,
        )

        # ======================================================
        # TREND ANALYSIS
        # ======================================================

        weekly = self.trend_engine.analyze(
            market_data["1W"],
            "1W"
        )

        daily = self.trend_engine.analyze(
            market_data["1D"],
            "1D"
        )

        h4 = self.trend_engine.analyze(
            market_data["4H"],
            "4H"
        )

        h1 = self.trend_engine.analyze(
            market_data["1H"],
            "1H"
        )

        m30 = self.trend_engine.analyze(
            market_data["30M"],
            "30M"
        )

        m15 = self.trend_engine.analyze(
            market_data["15M"],
            "15M"
        )

        # ======================================================
        # STORY
        # ======================================================

        context.story = self.story_engine.analyze(
            weekly,
            daily,
            h4,
        )

        # ======================================================
        # TRADING PLAN
        # ======================================================

        context.trading = self.trading_engine.analyze(
            h1,
            m30,
            m15,
        )

        # ======================================================
        # EXECUTION PLAN
        # ======================================================

        context.execution = self.execution_engine.analyze(
            context.manipulation,
            context.displacement,
            context.cisd,
            fvg_ready=False,
        )

        # ======================================================
        # PAL DECISION
        # ======================================================

        decision = self.pal_brain.analyze(
            context
        )

        # ======================================================
        # FINAL REPORT
        # ======================================================

        return self.report_engine.generate(
            context,
            decision,
        )