balance=1000
btc_position=0
last_signal=None

def execute_trade(signal,price):
    global balance
    global btc_position
    global last_signal

    if signal == last_signal:
        return
    
    if signal == "BUY" and balance > 0:
        btc_position=balance/price
        balance=0

        print(f"\n BUY EXECUTED")
        print(f"Bought BTC at {price}")
    
    elif signal == "SELL" and btc_position > 0:

        balance = btc_position * price
        btc_position = 0

        print(f"\n[SELL EXECUTED]")
        print(f"Sold BTC at {price}")

    last_signal = signal

def show_status(current_price):

    global balance
    global btc_position

    total_value = balance + (btc_position * current_price)

    print("\n===== ACCOUNT STATUS =====")
    print(f"Cash Balance : ${balance:.2f}")
    print(f"BTC Position : {btc_position:.6f}")
    print(f"Portfolio    : ${total_value:.2f}")

    