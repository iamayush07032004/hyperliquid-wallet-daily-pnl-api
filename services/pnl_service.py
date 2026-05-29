from datetime import datetime, timedelta


def build_daily_buckets(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    days = {}
    current = start

    while current <= end:
        key = current.strftime("%Y-%m-%d")

        days[key] = {
            "date": key,
            "realizedPnl": 0.0,
            "unrealizedPnl": 0.0,
            "fees": 0.0,
            "funding": 0.0,
            "netPnl": 0.0
        }

        current += timedelta(days=1)

    return days


def process_fills(days, fills):

    for fill in fills:

        if "time" not in fill:
            continue

        try:
            date = datetime.utcfromtimestamp(
                int(fill["time"]) / 1000
            ).strftime("%Y-%m-%d")

            if date not in days:
                continue

            pnl = float(fill.get("closedPnl", 0))
            fee = float(fill.get("fee", 0))

            days[date]["realizedPnl"] += pnl
            days[date]["fees"] += fee

        except Exception:
            continue


def process_funding(days, funding):

    for item in funding:

        if "time" not in item:
            continue

        try:
            date = datetime.utcfromtimestamp(
                int(item["time"]) / 1000
            ).strftime("%Y-%m-%d")

            if date not in days:
                continue

            amount = float(
                item.get("delta", {}).get("usdc", 0)
            )

            days[date]["funding"] += amount

        except Exception:
            continue


def calculate_net(days):

    for day in days.values():

        day["netPnl"] = (
            day["realizedPnl"]
            + day["unrealizedPnl"]
            - day["fees"]
            + day["funding"]
        )


def calculate_daily_pnl(
    fills,
    funding,
    start_date,
    end_date
):

    days = build_daily_buckets(
        start_date,
        end_date
    )

    process_fills(days, fills)
    process_funding(days, funding)

    calculate_net(days)

    return list(days.values())