from exchange import exchange
import pandas as pd
import time
from Paper import execute_trade,show_status
from Strategy import moving_average_strategy


symbol="PF_XBTUSD"
timeframe="1m"

while True:
        try:
            ohlcv=exchange.fetch_ohlcv(symbol,timeframe,limit=100)

            df=pd.DataFrame(
                ohlcv,
                columns=[
                    "timestamp",
                    "open",
                    "high",
                    "low",
                    "close",
                    "volume"
                ]
            )

            df["timestamp"]=pd.to_datetime(df["timestamp"],unit="ms")
            df["MA20"]=df["close"].rolling(window=20).mean()
            df["MA50"]=df["close"].rolling(window=50).mean()

            signal=moving_average_strategy(df)
            latest=df.iloc[-1]
            current_price=latest["close"]
            execute_trade(signal,current_price)
            show_status(current_price)

                

            time.sleep(10)

        except Exception as e:
             print(f"Error: {e}")
             time.sleep(5)
