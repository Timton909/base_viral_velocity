import requests, time

def viral_velocity():
    print("Base — Viral Velocity (holders +50/sec AND price +200% in 2 min)")
    history = {}

    while True:
        try:
            r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base")
            now = time.time()

            for pair in r.json().get("pairs", []):
                addr = pair["pairAddress"]
                holders = pair.get("holders", 0)
                change_5m = pair.get("priceChange", {}).get("m5", 0)
                age = now - pair.get("pairCreatedAt", 0) / 1000

                if age > 600: continue

                if addr not in history:
                    history[addr] = (now, holders)
                    continue

                last_t, last_h = history[addr]
                delta_t = now - last_t
                if delta_t < 120:
                    hps = (holders - last_h) / delta_t
                    if hps > 50 and change_5m > 200:
                        token = pair["baseToken"]["symbol"]
                        print(f"VIRAL VELOCITY MAX\n"
                              f"{token} — {hps:.0f} holders/sec + {change_5m:.0f}% price\n"
                              f"Total holders: {holders:,}\n"
                              f"https://dexscreener.com/base/{addr}\n"
                              f"→ This is escape velocity — real moonshot\n"
                              f"{'VIRAL'*30}")
                        del history[addr]

                history[addr] = (now, holders)

        except:
            pass
        time.sleep(4.8)

if __name__ == "__main__":
    viral_velocity()
