from analysis.pal_engine import PALEngine
from analysis.dxy_engine import DXYEngine
from analysis.execution_engine import ExecutionEngine
from analysis.market_health_engine import MarketHealthEngine
from analysis.news_engine import NewsEngine
from analysis.report_engine import ReportEngine

from services.ai_commentary_engine import AICommentaryEngine


class PALService:

    def __init__(self):

        self.pal_engine = PALEngine()
        self.dxy_engine = DXYEngine()
        self.execution_engine = ExecutionEngine()
        self.market_health_engine = MarketHealthEngine()
        self.news_engine = NewsEngine()
        self.ai_commentary_engine = AICommentaryEngine()
        self.report_engine = ReportEngine()

    def analyze(
        self,
        gbp_market,
        dxy_market,
        news_events,
        current_time
    ):

        # -----------------------------
        # PAL
        # -----------------------------

        pal = self.pal_engine.analyze(gbp_market)

        # -----------------------------
        # DXY
        # -----------------------------

        dxy = self.dxy_engine.analyze(dxy_market)

        # -----------------------------
        # Execution
        # -----------------------------

        execution = self.execution_engine.analyze(
            pal,
            dxy
        )

        # -----------------------------
        # Market Health
        # -----------------------------

        market_health = self.market_health_engine.analyze(
            pal,
            dxy
        )

        # -----------------------------
        # News
        # -----------------------------

        news = self.news_engine.analyze(
            news_events,
            current_time
        )

        # -----------------------------
        # Primary Workflow
        # -----------------------------

        primary = next(
            (
                tf for tf in pal.timeframes
                if tf.timeframe == "H4"
            ),
            pal.timeframes[0]
        )

        # -----------------------------
        # AI Commentary
        # -----------------------------

        ai_commentary = self.ai_commentary_engine.generate(

            workflow={
                "trend": pal.overall_bias,
                "stage": primary.story.stage,
                "next_step": primary.story.next_step,
                "completed_steps": primary.story.completed_steps,
                "missing_steps": primary.story.missing_steps,
            },

            execution={
                "action": execution.action,
                "reason": execution.reason,
            },

            market_health=market_health,

            dxy={
                "aligned": dxy.gbp_alignment,
            },

            news=news,
        )

        # -----------------------------
        # Final Report
        # -----------------------------

        return self.report_engine.build(
            symbol=gbp_market.symbol,
            pal=pal,
            dxy=dxy,
            execution=execution,
            market_health=market_health,
            news=news,
            ai_commentary=ai_commentary,
        )