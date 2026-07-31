from datetime import datetime


class NewsEngine:
    """
    PAL News Engine

    Evaluates scheduled economic news and determines
    whether trading conditions are safe.
    """

    HIGH_IMPACT = {

        "CPI",
        "Core CPI",
        "PPI",
        "Core PCE",

        "NFP",
        "Employment Change",
        "Unemployment Rate",

        "Interest Rate Decision",
        "FOMC",
        "Fed",
        "BoE",
        "ECB",

        "GDP",
        "PMI",
        "Retail Sales"

    }

    NEWS_BLACKOUT_MINUTES = 30

    def analyze(
        self,
        events: list[dict],
        now: datetime
    ) -> dict:

        result = {

            "safe_to_trade": True,

            "high_impact": [],

            "warnings": [],

            "minutes_to_next_news": None,

            "summary": ""

        }

        nearest_minutes = None

        for event in events:

            impact = event.get("impact", "")
            title = event.get("title", "")
            event_time = event.get("time")

            if impact != "High":
                continue

            if title not in self.HIGH_IMPACT:
                continue

            if event_time is None:
                continue

            minutes = abs(
                (event_time - now).total_seconds()
            ) / 60

            if nearest_minutes is None or minutes < nearest_minutes:

                nearest_minutes = minutes

            if minutes <= self.NEWS_BLACKOUT_MINUTES:

                result["safe_to_trade"] = False

                result["high_impact"].append(

                    {

                        "title": title,
                        "time": event_time,
                        "minutes": round(minutes)

                    }

                )

                result["warnings"].append(

                    f"{title} within "
                    f"{self.NEWS_BLACKOUT_MINUTES} minutes."

                )

        result["minutes_to_next_news"] = nearest_minutes

        if result["safe_to_trade"]:

            if nearest_minutes is None:

                result["summary"] = (
                    "No scheduled high-impact news."
                )

            else:

                result["summary"] = (
                    f"Safe to trade. "
                    f"Next high-impact news in "
                    f"{round(nearest_minutes)} minutes."
                )

        else:

            result["summary"] = (
                "Trading paused due to nearby high-impact news."
            )

        return result