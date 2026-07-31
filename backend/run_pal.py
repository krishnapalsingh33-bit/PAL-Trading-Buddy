from config.settings import TWELVE_DATA_API_KEY

from services.market_data_service import MarketDataService

from analysis.timeframe_loader import TimeframeLoader
from analysis.pal_engine import PalEngine


def line():

    print("-" * 60)


def section(title):

    print()
    print(title)
    line()


def main():

    print()
    print("=" * 60)
    print("PAL MARKET BRIEF")
    print("=" * 60)

    service = MarketDataService(

        TWELVE_DATA_API_KEY

    )

    loader = TimeframeLoader(

        service

    )

    market = loader.load(

        "GBP/USD"

    )

    pal = PalEngine()

    result = pal.analyze(

        market

    )

    mission = result["mission"]
    story = result["story"]
    execution = result["execution"]
    brief = result["brief"]

    # -----------------------------------
    # Session
    # -----------------------------------

    section("SESSION")

    print(brief.session)

    # -----------------------------------
    # Mission
    # -----------------------------------

    section("CURRENT MISSION")

    print(brief.mission)

    # -----------------------------------
    # Story
    # -----------------------------------

    section("CURRENT STORY")

    print(story.description)

    # -----------------------------------
    # Execution
    # -----------------------------------

    section("EXECUTION")

    print(execution.stage)

    # -----------------------------------
    # Next Step
    # -----------------------------------

    section("NEXT STEP")

    print(story.next_step)

    # -----------------------------------
    # Confidence
    # -----------------------------------

    section("CONFIDENCE")

    print(f"{execution.confidence}%")

    # -----------------------------------
    # Evidence
    # -----------------------------------

    section("WHY")

    if brief.evidence:

        for item in brief.evidence:

            print(f"• {item}")

    else:

        print("No evidence available.")

    print()
    print("=" * 60)


if __name__ == "__main__":

    main()