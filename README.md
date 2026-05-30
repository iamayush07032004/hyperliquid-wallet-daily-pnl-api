# Hyperliquid Wallet Daily PnL API

A FastAPI backend service that calculates daily Profit & Loss (PnL) for a Hyperliquid wallet over a specified date range.

## Features

- Calculate daily wallet PnL
- Fetch trading fills and funding data
- Date range based reporting
- Input validation
- Unit tests included
- Interactive API documentation with Swagger

## Installation

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
GET /api/hyperliquid/0x5078c2fbea2b2ad61bc840bc023e35fce56bedb6/pnl?start=2026-01-01&end=2026-01-31
```

## Test Data

### Wallet

```text
0x5078c2fbea2b2ad61bc840bc023e35fce56bedb6
```

### Date Ranges

| Start Date | End Date |
|------------|----------|
| 2025-07-01 | 2025-07-31 |
| 2025-07-10 | 2025-07-20 |
| 2026-01-01 | 2026-01-31 |

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
