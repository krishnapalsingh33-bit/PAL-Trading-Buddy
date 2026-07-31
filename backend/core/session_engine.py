from dataclasses import dataclass
from datetime import datetime


@dataclass
class SessionData:

    name: str
    greeting: str
    briefing_type: str
    focus: str


def analyze_session():

    """
    Trading sessions based on India time (IST).
    """

    now = datetime.now()

    hour = now.hour
    minute = now.minute

    current = hour * 60 + minute

    # -----------------------------
    # Asia
    # -----------------------------
    if current < 735:

        return SessionData(

            name="Asia Session",

            greeting="Good Morning Krishna",

            briefing_type="Preparation",

            focus="Build today's market story."

        )

    # -----------------------------
    # London
    # -----------------------------
    elif current < 1080:

        return SessionData(

            name="London Session",

            greeting="Good Afternoon Krishna",

            briefing_type="Execution",

            focus="Wait for your A++ setup."

        )

    # -----------------------------
    # New York
    # -----------------------------
    else:

        return SessionData(

            name="New York Session",

            greeting="Good Evening Krishna",

            briefing_type="Management",

            focus="Manage or complete today's idea."

        )