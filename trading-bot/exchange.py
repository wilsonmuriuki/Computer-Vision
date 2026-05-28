import ccxt
from config import API_KEY,SECRET_KEY

exchange=ccxt.krakenfutures({
    "apiKey":API_KEY,
    "secret":SECRET_KEY,
    "enableRateLimit":True
})
