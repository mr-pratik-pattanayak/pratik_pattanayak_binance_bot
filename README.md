
# 📊 Binance Futures Testnet CLI Trading Bot

**Author:** Pratik Pattanayak  
**Platform:** Binance USDT-M Futures Testnet  
**Language:** Python 3

## 📌 Overview

This is a CLI-based trading bot for Binance USDT-M Futures Testnet.  
It allows you to place the following order types directly via terminal:

- ✅ Market Orders
- ✅ Limit Orders (with notional validation)
- ✅ Simulated OCO (One Cancels the Other) Orders
- ✅ TWAP (Time-Weighted Average Price) Orders
- ✅ Grid Trading Orders (buy/sell limit grid)

All trades, errors, and API interactions are logged for auditing.

## 📦 Features

- **Secure API key management via `.env`**
- **Live Market Price validation for OCO orders**
- **Notional check for Limit orders (≥ 100 USDT)**
- **CLI Menu-based system**
- **Structured logging to `bot.log`**
- **Compatible with Binance Futures Testnet**

## ⚙️ Installation

### 1️⃣ Clone the project
```bash
git clone <your-repo-link>
cd pratik_pattanayak_binance_bot
```

### 2️⃣ Create a Virtual Environment (optional)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Required Packages
```bash
pip install -r requirements.txt
```

## 📑 Environment Setup

Create a `.env` file in your project root:

```
API_KEY=your_testnet_api_key_here
API_SECRET=your_testnet_secret_here
```

You can get these keys from:  
https://testnet.binancefuture.com/en/futures/api-management

## 📊 Usage Instructions

### Run the CLI bot:
```bash
python src/cli_main.py
```

### Menu Options:
```
===== Binance Futures CLI Bot =====
1. Place Market Order
2. Place Limit Order
3. Place OCO Order
4. Place TWAP Order
5. Place Grid Orders
6. Exit
```

## 📄 Examples

**Market Order, Limit Order, OCO, TWAP, and Grid order usage examples provided.**

## 📁 Project Structure

Clean folder structure with modules for Market, Limit, OCO, TWAP, Grid orders and CLI.

## 📝 Logs

All API actions and errors logged in `bot.log`.

## 📌 Requirements

```
python-binance==1.0.17
python-dotenv==1.0.1
```



