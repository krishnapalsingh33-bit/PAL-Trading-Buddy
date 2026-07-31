from datetime import datetime

from fastapi import APIRouter

from services.pal_service import PALService
from data.market_provider import get_symbol_data

router = APIRouter(
    prefix="/pal",
    tags=["PAL Trading Buddy"]
)

service = PALService()


@router.get("/analyze/{symbol}")
def analyze(symbol: str):

    gbp_market = get_symbol_data(symbol)

    dxy_market = get_symbol_data("USDX")

    news_events = []

    report = service.analyze(

        gbp_market=gbp_market,

        dxy_market=dxy_market,

        news_events=news_events,

        current_time=datetime.utcnow()

    )

    return {

        "success": True,

        "symbol": symbol.upper(),

        "timestamp": datetime.utcnow().isoformat(),

        "report": report

    }