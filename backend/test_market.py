from config.settings import TWELVE_DATA_API_KEY

from services.market_data_service import MarketDataService

from analysis.timeframe_loader import TimeframeLoader

from analysis.pal_engine import PalEngine

from models.mission import Mission


service = MarketDataService(

    TWELVE_DATA_API_KEY

)

market = TimeframeLoader(

    service

).load(

    "GBP/USD"

)

mission = Mission(

    target_timeframe="Daily",

    target_side="BUY",

    reason="Testing"

)

pal = PalEngine()

result = pal.analyze(

    market,

    mission

)

print()

print("=" * 60)

print("PAL ENGINE")

print("=" * 60)

print()

print(result["mission"])

print()

print(result["context"].daily)