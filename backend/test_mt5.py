import MetaTrader5 as mt5

if not mt5.initialize():
    print(mt5.last_error())
    quit()

for symbol in [
    "DX",
    "USDX",
    "GDXY",
    "DXYN",
    "DXYZ",
]:
    print("=" * 40)
    print(symbol)

    if mt5.symbol_select(symbol, True):

        rates = mt5.copy_rates_from_pos(
            symbol,
            mt5.TIMEFRAME_H1,
            0,
            3,
        )

        if rates is None:
            print("No data")
        else:
            print(rates)

    else:
        print("Cannot select")

mt5.shutdown()