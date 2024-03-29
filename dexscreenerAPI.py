import requests



class DexScreenerAPI:
    def __init__(self):
        self.url = 'https://api.dexscreener.com/v1'

    def get_price_data(self):
    # def get_price_data(self, coinContrat):
        price_data = {}

        # Add indented block of code here

        # for token in MONITORED_TOKENS:
        # token = coinContrat
        # token = "0x6e958411b96081C2A0BeC3ADe9a59aBd3Bb89680"
        token = "0x118e37aff646d58707d553f39293feffd4be1a2b"
        try:
            url = f"https://api.dexscreener.com/latest/dex/pairs/bsc/{token.upper()}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data and data.get('pairs', []):
                price_data[token] = {
                    'lastPrice': float(data['pairs'][0]['priceUsd']),
                    'symbol': data['pairs'][0]['baseToken'].get('symbol')
                }
            else:
                print(f"'{token}' tokeni API cevabında bulunamadı veya fiyat verisi mevcut değil.")
                price_data[token] = {'lastPrice': None}

        except requests.exceptions.RequestException as e:
            print(f"'{token}' için fiyat verisi alınırken hata oluştu: {e}")
            price_data[token] = {'lastPrice': None}

        latest_price = price_data.get(token, {}).get("lastPrice")

        return [latest_price, token]
    
# print(DexScreenerAPI().get_price_data())