# Hyperliquid Wallet Daily PnL API

A FastAPI backend service that calculates daily Profit & Loss (PnL) for a Hyperliquid wallet over a specified date range.

## Features

- Calculate daily wallet PnL
- Fetch trading fills and funding data
- Date range based reporting
- Input validation
- Unit tests included
- Interactive API documentation with Swagger

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app:app --reload
```

Application URL:

```text
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Endpoint

```http
GET /api/hyperliquid/{wallet}/pnl
```

### Example Request

```http
GET /api/hyperliquid/0x5078c2fbea2b2ad61bc840bc023e35fce56bebdb/pnl?start=2026-01-01&end=2026-01-31
```

### Query Parameters

| Parameter | Description |
|------------|-------------|
| wallet | 0x5078c2fbea2b2ad61bc840bc023e35fce56bedb6 |
1=| start | Start date (2025-07-01) |, 2=| Start date (2025-07-10) |, 3=| Start date (2026-01-01) |
1=| end | End date (2025-07-31) |, 2=| End date (2025-07-20) |, 3=| End date (2026-01-31) |

## Run Tests

```bash
pytest
```

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pytest

## Repository

GitHub Repository:

https://github.com/iamayush07032004/hyperliquid-wallet-daily-pnl-api
