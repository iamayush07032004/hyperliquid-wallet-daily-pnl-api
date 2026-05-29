from services.hyperliquid_service import HyperLiquidService

hl = HyperLiquidService()

wallet = "0x5078c2fbea2b2ad61bc840bc023e35fce56bedb6"

fills = hl.get_user_fills(wallet)

print(fills)
print("COUNT =", len(fills))