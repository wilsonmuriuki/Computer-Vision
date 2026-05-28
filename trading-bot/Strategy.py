def moving_average_strategy(df):
    latest=df.iloc[-1]
    ma20=latest["MA20"]
    ma50=latest["MA50"]

    if ma20 > ma50:
        return "BUY"
    elif ma20 < ma50:
        return "SELL"
    return "HOLD"