import re


def validate_wallet(wallet: str) -> bool:
    pattern = r"^0x[a-fA-F0-9]{40}$"
    return bool(re.match(pattern, wallet))