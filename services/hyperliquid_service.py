import requests


class HyperLiquidService:

    BASE_URL = "https://api.hyperliquid.xyz/info"

    def _post(self, payload):

        response = requests.post(
            self.BASE_URL,
            json=payload,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    def get_user_fills(self, wallet):

        payload = {
            "type": "userFills",
            "user": wallet
        }

        return self._post(payload)

    def get_user_funding(self, wallet):

        payload = {
            "type": "userFunding",
            "user": wallet
        }

        return self._post(payload)