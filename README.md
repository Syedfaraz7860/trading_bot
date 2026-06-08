# Binance Spot Testnet Trading Bot

A simple Python-based trading bot for Binance Spot Testnet. This bot allows users to place MARKET and LIMIT orders directly from the command line using Binance API.

## Features

* Place Market Buy/Sell Orders
* Place Limit Buy/Sell Orders
* Command Line Interface (CLI)
* Environment Variable Support using `.env`
* Logging Support
* Input Validation
* Modular Project Structure

## Project Structure

```text
trading-bot/
│
├── .env
├── logs/
│   └── trading_bot.log
│
└── bot/
    ├── cli.py
    ├── client.py
    ├── orders.py
    ├── validators.py
    └── logging_config.py
```

## Requirements

* Python 3.10+
* Binance Testnet Account

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd trading-bot
```

Install dependencies:

```bash
pip install python-binance python-dotenv
```

## Environment Variables

Create a `.env` file in the project root directory.

```env
API_KEY=YOUR_BINANCE_API_KEY
API_SECRET=YOUR_BINANCE_SECRET_KEY
```

## Running the Bot

### Market Buy Order

```bash
python bot/cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Market Sell Order

```bash
python bot/cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Limit Buy Order

```bash
python bot/cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### Limit Sell Order

```bash
python bot/cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 100000
```

## Example Output

```text
ORDER SUCCESS

Order ID : 1880781
Status : FILLED
Executed Qty : 0.00100000
```

## Logging

All trading activities are stored in:

```text
logs/trading_bot.log
```

Logs include:

* Order Requests
* Order Responses
* Errors and Exceptions

## Security Notes

* Never commit `.env` files to GitHub.
* Never share API Secret Keys publicly.
* Add `.env` to `.gitignore`.

Example:

```gitignore
.env
```

## Future Enhancements

* Balance Checking
* Open Orders Management
* Order Cancellation
* Telegram Notifications
* RSI Strategy
* EMA Crossover Strategy
* Risk Management Module
* Docker Support
* AWS Deployment

## Author

Syed Farazdakmehdi

## License

This project is for educational and learning purposes.
