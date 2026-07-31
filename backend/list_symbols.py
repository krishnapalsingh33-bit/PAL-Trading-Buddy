import MetaTrader5 as mt5

if not mt5.initialize():
    print(mt5.last_error())
    quit()

symbols = mt5.symbols_get()

for s in symbols:
    name = s.name.upper()
    if (
        "USD" in name
        or "DXY" in name
        or "INDEX" in name
        or "DX" == name
    ):
        print(s.name)

mt5.shutdown()