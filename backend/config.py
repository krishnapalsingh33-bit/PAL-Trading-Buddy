from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv(Path(__file__).parent.parent / ".env")


class Settings:

    APP_NAME = os.getenv("APP_NAME", "PAL Trading Buddy")

    DEBUG = os.getenv("DEBUG", "False") == "True"

    DEFAULT_SYMBOL = os.getenv("DEFAULT_SYMBOL", "GBPUSD")

    DXY_SYMBOL = os.getenv("DXY_SYMBOL", "DXY")

    DATA_PROVIDER = os.getenv("DATA_PROVIDER", "tradingview")

    TIMEZONE = os.getenv("TIMEZONE", "UTC")


settings = Settings()