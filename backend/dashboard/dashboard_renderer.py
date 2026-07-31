class DashboardRenderer:

    def render(

        self,

        story,

        trading,

        execution,

        dxy=None,

        news=None

    ) -> str:

        lines = []

        lines.append("=" * 60)
        lines.append("PAL MARKET BRIEF")
        lines.append("=" * 60)
        lines.append("")

        # --------------------------------------------------
        # STORY
        # --------------------------------------------------

        lines.append("STORY")
        lines.append("-" * 60)

        lines.append(f"Weekly : {story.weekly_trend}")
        lines.append(f"Daily  : {story.daily_trend}")
        lines.append(f"4H     : {story.h4_trend}")

        lines.append("")
        lines.append("Market Story")

        lines.append(story.market_story)

        lines.append("")

        lines.append(
            f"Confidence : {story.confidence}%"
        )

        lines.append("")
        lines.append("=" * 60)

        # --------------------------------------------------
        # TRADING
        # --------------------------------------------------

        lines.append("TRADING")
        lines.append("-" * 60)

        lines.append(f"1H  : {trading.h1_trend}")
        lines.append(f"30M : {trading.m30_trend}")
        lines.append(f"15M : {trading.m15_trend}")

        lines.append("")
        lines.append("Mission")

        lines.append(trading.current_mission)

        lines.append("")
        lines.append("=" * 60)

        # --------------------------------------------------
        # EXECUTION
        # --------------------------------------------------

        lines.append("EXECUTION")
        lines.append("-" * 60)

        lines.append(
            f"Stage : {execution.stage}"
        )

        lines.append(
            f"Ready : {execution.ready}"
        )

        lines.append(
            f"Confidence : {execution.confidence}%"
        )

        lines.append("")

        for item in execution.reason:

            lines.append(f"• {item}")

        lines.append("")
        lines.append("=" * 60)

        # --------------------------------------------------
        # DXY
        # --------------------------------------------------

        if dxy:

            lines.append("DXY STATUS")
            lines.append("-" * 60)

            lines.append(
                f"Bias : {dxy.bias}"
            )

            lines.append(
                f"Strength : {dxy.strength}"
            )

            lines.append(
                f"Objective : {dxy.objective}"
            )

            lines.append("")
            lines.append("=" * 60)

        # --------------------------------------------------
        # NEWS
        # --------------------------------------------------

        if news:

            lines.append("NEWS & EVENTS")
            lines.append("-" * 60)

            for event in news:

                lines.append(event)

            lines.append("")
            lines.append("=" * 60)

        return "\n".join(lines)