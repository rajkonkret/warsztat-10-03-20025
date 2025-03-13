import time
import requests as re

url = 'https://api.nbp.pl/api/exchangerates/rates/A/EUR/'

def multiple_requests():
    start_time = time.time()

    for _ in range(100):
        response = re.get(url)
        print(response.json())

    elapsed = time.time() - start_time
    print(f"Requests time: {elapsed:.4f}s")


multiple_requests()
# 1 : Requests time: 0.0380s
# 2 Requests time: 3.5301s