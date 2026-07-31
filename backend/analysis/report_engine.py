from datetime import datetime

from models.pal_report import PALReport
from models.execution_decision import ExecutionDecision
from models.pal_analysis import PALAnalysis
from models.dxy_analysis import DXYAnalysis


class ReportEngine:
    """
    PAL Report Engine

    Converts every engine output into a clean,
    frontend-friendly dashboard response.
    """

    def build(
        self,
        symbol: str,
        pal: PALAnalysis,
        dxy: DXYAnalysis,
        execution: ExecutionDecision,
        market_health,
        news,
        ai_commentary
    ) -> PALReport:

        report = PALReport()

        report.symbol = symbol.upper()
        report.timestamp = datetime.utcnow().isoformat()
        report.success = True

        # ==========================================================
        # MARKET OVERVIEW
        # ==========================================================

        report.market_health = {

            "status": market_health.get("status"),
            "score": market_health.get("score"),
            "summary": market_health.get("summary")

        }

        # ==========================================================
        # NEWS
        # ==========================================================

        report.news = {

            "safe_to_trade": news.get("safe_to_trade"),
            "summary": news.get("summary"),
            "warnings": news.get("warnings", []),
            "high_impact": news.get("high_impact", [])

        }

        # ==========================================================
        # PAL OVERVIEW
        # ==========================================================

        report.pal = {

            "overall_bias": pal.overall_bias,
            "execution_timeframe": pal.execution_timeframe,
            "ready_for_entry": pal.ready_for_entry,

            "workflow": [

                {

                    "timeframe": tf.timeframe,

                    "trend": tf.story.trend,

                    "stage": tf.story.stage,

                    "grade": tf.grade.grade,

                    "decision": tf.grade.decision,

                    "next_step": tf.story.next_step,

                    "completed_steps": tf.story.completed_steps,

                    "missing_steps": tf.story.missing_steps

                }

                for tf in pal.timeframes

            ]

        }

        # ==========================================================
        # DXY
        # ==========================================================

        report.dxy = {

            "trend": dxy.trend,

            "expected_gbp_direction": dxy.expected_gbp_direction,

            "aligned": dxy.gbp_alignment,

            "confirmations": dxy.confirmations,

            "summary": dxy.summary

        }

        # ==========================================================
        # EXECUTION
        # ==========================================================

        report.execution = {

            "action": execution.action,

            "trend": execution.trend,

            "timeframe": execution.timeframe,

            "stage": execution.stage,

            "reason": execution.reason,

            "confirmations": execution.confirmations,

            "summary": execution.summary

        }

        # ==========================================================
        # AI COMMENTARY
        # ==========================================================

        report.ai_commentary = ai_commentary

        # ==========================================================
        # DASHBOARD
        # ==========================================================

        report.summary = {

            "market": {

                "bias": pal.overall_bias,

                "health": market_health.get("status"),

                "safe_to_trade": news.get("safe_to_trade")

            },

            "execution": {

                "action": execution.action,

                "stage": execution.stage,

                "reason": execution.reason

            },

            "dxy": {

                "trend": dxy.trend,

                "aligned": dxy.gbp_alignment

            }

        }

        return report