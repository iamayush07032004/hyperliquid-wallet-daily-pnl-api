from fastapi import FastAPI
from fastapi import HTTPException

from utils.validators import validate_wallet

from services.hyperliquid_service import (
    HyperLiquidService
)

from services.pnl_service import (
    calculate_daily_pnl
)

app = FastAPI()

hl = HyperLiquidService()


@app.get(
    "/api/hyperliquid/{wallet}/pnl"
)
def get_pnl(
    wallet: str,
    start: str,
    end: str
):

    if not validate_wallet(wallet):

        raise HTTPException(
            status_code=400,
            detail="Invalid wallet"
        )

    fills = hl.get_user_fills(wallet)
    funding = hl.get_user_funding(wallet)

    result = calculate_daily_pnl(
        fills,
        funding,
        start,
        end
    )

    return {
        "wallet": wallet,
        "start": start,
        "end": end,
        "daily": result
    }