from services.market_data_service import MarketDataService
from engines.gbpusd_engine import GBPUSDEngine


def main():

    market = MarketDataService()

    data = market.get_market_data("GBPUSD")

    print("=" * 50)
    print("CANDLE COUNTS")
    print("=" * 50)

    print(f"Monthly : {len(data.monthly)}")
    print(f"Weekly  : {len(data.weekly)}")
    print(f"Daily   : {len(data.daily)}")
    print(f"H4      : {len(data.h4)}")
    print(f"H1      : {len(data.h1)}")
    print(f"M30     : {len(data.m30)}")
    print(f"M15     : {len(data.m15)}")
    print(f"M5      : {len(data.m5)}")
    print(f"M3      : {len(data.m3)}")
    print(f"M1      : {len(data.m1)}")

    print()

    engine = GBPUSDEngine()

    analysis = engine.analyze(
        data.h1,
        "H1",
    )

    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)

    print(analysis.summary)


if __name__ == "__main__":
    main()