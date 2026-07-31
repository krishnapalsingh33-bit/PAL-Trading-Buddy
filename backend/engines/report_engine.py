from models.pal_context import PALContext
from models.pal_decision import PALDecision


class ReportEngine:
    """
    Generates the final PAL MARKET BRIEF.
    """

    def generate(
        self,
        context: PALContext,
        decision: PALDecision,
    ) -> str:

        story = context.story
        trading = context.trading
        execution = context.execution

        weekly_trend = "-"
        daily_trend = "-"
        h4_trend = "-"

        if story:

            if story.weekly:
                weekly_trend = story.weekly.direction

            if story.daily:
                daily_trend = story.daily.direction

            if story.h4:
                h4_trend = story.h4.direction

        h1_trend = "-"
        m30_trend = "-"
        m15_trend = "-"

        if trading:

            if trading.h1:
                h1_trend = trading.h1.direction

            if trading.m30:
                m30_trend = trading.m30.direction

            if trading.m15:
                m15_trend = trading.m15.direction

        manipulation = "Waiting"
        displacement = "Waiting"
        fvg = "Waiting"
        cisd = "Waiting"

        if execution:

            manipulation = (
                "Ready"
                if execution.manipulation_ready
                else "Waiting"
            )

            displacement = (
                "Ready"
                if execution.displacement_ready
                else "Waiting"
            )

            fvg = (
                "Ready"
                if execution.fvg_ready
                else "Waiting"
            )

            cisd = (
                "Ready"
                if execution.cisd_ready
                else "Waiting"
            )

        return f"""
==========================================================
                    PAL MARKET BRIEF
==========================================================

STORY
----------------------------------------------------------

Weekly Trend      : {weekly_trend}
Daily Trend       : {daily_trend}
4H Trend          : {h4_trend}

Market Story

{decision.market_story}

Confidence : {decision.confidence}%

==========================================================

TRADING
----------------------------------------------------------

1H Trend          : {h1_trend}
30M Trend         : {m30_trend}
15M Trend         : {m15_trend}

Mission

{decision.mission}

Trading Focus

{decision.trading_focus}

==========================================================

EXECUTION
----------------------------------------------------------

Manipulation      : {manipulation}
Displacement      : {displacement}
FVG               : {fvg}
CISD              : {cisd}

Action

{decision.action}

==========================================================

DXY STATUS
----------------------------------------------------------

Bias              : -
Strength          : -
Objective         : -

Correlation

-

GBP/USD Expected

-

==========================================================

NEWS & EVENTS
----------------------------------------------------------

High Impact

-

Notes

-

==========================================================

MARKET HEALTH
----------------------------------------------------------

Liquidity         : -

Volatility        : -

Trend Quality     : -

News Risk         : -

Trading Conditions

-

==========================================================

NEXT EVENT
----------------------------------------------------------

{decision.next_event}

==========================================================
"""