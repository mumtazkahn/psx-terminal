# PSX Trading Platform API Documentation

## General Information

* Base endpoint: `https://psxterminal.com`
* WebSocket endpoint: `wss://psxterminal.com/`
* REST API timestamps are in Unix time format (seconds)
* WebSocket timestamps are in Unix time format (milliseconds)
* All symbol names are case-sensitive

## REST API

### Market Data Endpoints

#### Test Connectivity
```
GET /api/status
```
Test connectivity to the REST API.

**Response:**
```json
{
  "status": "ok",
  "timestamp": 1750762129,
  "uptime": 1234.567
}
```

#### Single Symbol Market Data
```
GET /api/ticks/{type}/{symbol}
```
Get real-time market data for a specific symbol.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| type | STRING | YES | Market type (REG, FUT, IDX, ODL, BNB) |
| symbol | STRING | YES | Symbol name (e.g., HUBC) |

**Response:**
```json
{
  "success": true,
  "data": {
    "market": "REG",
    "st": "SUS",
    "symbol": "HUBC",
    "price": 164.42,
    "change": 3.11,
    "changePercent": 0.01928,
    "volume": 12573014,
    "trades": 8460,
    "value": 2082312049.64,
    "high": 167.84,
    "low": 162.11,
    "bid": 0,
    "ask": 0,
    "bidVol": 0,
    "askVol": 0,
    "timestamp": 1756205291
  },
  "timestamp": 1756233149809
}
```

#### Symbol List
```
GET /api/symbols
```
Get all available trading symbols.

**Response:**
```json
{
  "success": true,
  "data": ["786", "AABS", "AATM", "ABL", "ABOT", "ACI"],
  "timestamp": 1756233194813
}
```

#### Market Statistics
```
GET /api/stats/{type}
```
Get market statistics and breadth indicators for a specific type.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| type | STRING | YES | Stats type (REG, IDX, BNB, ODL, FUT, breadth, sectors) |

**Response (REG stats):**
```json
{
  "success": true,
  "data": {
    "totalVolume": 1000000000,
    "totalValue": 50000000000,
    "totalTrades": 15000,
    "symbolCount": 500,
    "gainers": 250,
    "losers": 200,
    "unchanged": 50,
    "topGainers": [
      {
        "symbol": "SYMBOL",
        "change": 5.50,
        "changePercent": 10.5,
        "price": 58.0,
        "volume": 100000,
        "value": 5800000
      }
    ],
    "topLosers": [...]
  },
  "timestamp": 1750762129
}
```

**Response (breadth stats):**
```json
{
  "success": true,
  "data": {
    "advances": 250,
    "declines": 200,
    "unchanged": 50,
    "advanceDeclineRatio": 1.25,
    "advanceDeclineSpread": 50,
    "advanceDeclinePercent": 50.0,
    "upVolume": 600000000,
    "downVolume": 400000000,
    "upDownVolumeRatio": 1.5
  },
  "timestamp": 1750762129
}
```

**Response (sectors stats):**
```json
{
  "success": true,
  "data": {
    "BANKING": {
      "totalVolume": 200000000,
      "totalValue": 10000000000,
      "totalTrades": 3000,
      "gainers": 15,
      "losers": 10,
      "unchanged": 5,
      "avgChange": 2.5,
      "avgChangePercent": 1.8,
      "symbols": ["HBL", "UBL", "MCB"]
    }
  },
  "timestamp": 1750762129
}
```

#### Company Information
```
GET /api/companies/{symbol}
```
Get detailed company information including financial stats and business description.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| symbol | STRING | YES | Symbol name (e.g., FFC) |

**Response:**
```json
{
  "success": true,
  "data": {
    "symbol": "FFC",
    "scrapedAt": "2025-06-26T19:01:05.006Z",
    "financialStats": {
      "marketCap": {
        "raw": "538,077,397.96",
        "numeric": 538077397.96
      },
      "shares": {
        "raw": "1,423,108,696",
        "numeric": 1423108696
      },
      "freeFloat": {
        "raw": "853,865,218",
        "numeric": 853865218
      },
      "freeFloatPercent": {
        "raw": "60.00%",
        "numeric": 60
      }
    },
    "businessDescription": "Fauji Fertilizer Company Limited is a public company incorporated in Pakistan under the Companies Act, 1913, (now the Companies Act, 2017). The principal activity of the Company is manufacturing, purchasing and marketing of fertilizers and chemicals, including investment in other fertilizer, chemical, cement, energy generation, food processing and banking operations.",
    "keyPeople": [
      {
        "name": "Jahangir Piracha",
        "position": "CEO"
      },
      {
        "name": "Lt. Gen. Anwar Ali Hyder, HI (M) (Retd.)",
        "position": "Chairperson"
      },
      {
        "name": "Brig Khurram Shahzada, SI(M), (Retd)",
        "position": "Company Secretary"
      }
    ],
    "error": null
  },
  "timestamp": 1756233234002
}
```

#### Fundamentals Data
```
GET /api/fundamentals/{symbol}
```
Get fundamental analysis data and financial ratios for a specific symbol.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| symbol | STRING | YES | Symbol name (e.g., HUBC) |

**Response:**
```json
{
  "success": true,
  "data": {
    "symbol": "HUBC",
    "sector": "0824",
    "listedIn": "ALLSHR,KMI30,KMIALLSHR,KSE100,KSE100PR,KSE30,MII30,MZNPI,NBPPGI,NITPGI,PSXDIV20,UPP9",
    "marketCap": "213.3B",
    "price": 164.42,
    "changePercent": 1.928,
    "yearChange": 6.52413346290897,
    "peRatio": 6.990646258503401,
    "dividendYield": 9.22635319846911,
    "freeFloat": "908.0M",
    "volume30Avg": 6290340.63,
    "isNonCompliant": false,
    "timestamp": "2025-08-26T17:51:47.106Z"
  },
  "timestamp": 1756233247975
}
```

### K-Line/Candlestick Data Endpoints

#### Get K-Lines with Range/Limit
```
GET /api/klines/{symbol}/{timeframe}
```
Get historical candlestick/kline data for a symbol and timeframe.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| symbol | STRING | YES | Symbol name (e.g., HUBC) |
| timeframe | STRING | YES | Time interval (1m, 5m, 15m, 1h, 4h, 1d) |
| start | STRING | NO | Start timestamp (13-digit Unix timestamp in milliseconds) |
| end | STRING | NO | End timestamp (13-digit Unix timestamp in milliseconds) |
| limit | INTEGER | NO | Number of records to return (max: 100, default: varies) |

**Response (with limit):**
```json
{
  "success": true,
  "data": [
    {
      "symbol": "HUBC",
      "timeframe": "1h",
      "timestamp": 1755237600000,
      "open": 160.2,
      "high": 160.89,
      "low": 158.4,
      "close": 159,
      "volume": 995047
    }
  ],
  "count": 50,
  "symbol": "HUBC",
  "timeframe": "1h",
  "startTimestamp": null,
  "endTimestamp": null,
  "timestamp": 1756233269601
}
```

**Response (with timestamp range):**
```json
{
  "success": true,
  "data": [
    {
      "symbol": "HUBC",
      "timeframe": "1h",
      "timestamp": 1756098000000,
      "open": 162.6,
      "high": 162.6,
      "low": 161,
      "close": 161.7,
      "volume": 458744
    }
  ],
  "count": 10,
  "symbol": "HUBC",
  "timeframe": "1h",
  "startTimestamp": "1756000000000",
  "endTimestamp": "1756200000000",
  "timestamp": 1756233443096
}
```

#### Get Single K-Line by Exact Timestamp
```
GET /api/klines/{symbol}/{timeframe}/{timestamp}
```
Get a single candlestick/kline data point for an exact timestamp.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| symbol | STRING | YES | Symbol name (e.g., HUBC) |
| timeframe | STRING | YES | Time interval (1m, 5m, 15m, 1h, 4h, 1d) |
| timestamp | STRING | YES | Exact timestamp (13-digit Unix timestamp in milliseconds) |

**Response:**
```json
{
  "success": true,
  "data": {
    "symbol": "HUBC",
    "timeframe": "1h",
    "timestamp": 1756202400000,
    "open": 165,
    "high": 165,
    "low": 164,
    "close": 164.42,
    "volume": 824020
  },
  "timestamp": 1756233302714
}
```

### Dividend Data Endpoints

#### Get Dividends for Symbol
```
GET /api/dividends/{symbol}
```
Get dividend history for a specific symbol (last 12 months for public access).

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| symbol | STRING | YES | Symbol name (e.g., MARI) |

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "symbol": "MARI",
      "ex_date": "2025-09-18",
      "payment_date": "2025-10-17",
      "record_date": "2025-09-19",
      "amount": 21.7,
      "year": 2025
    },
    {
      "symbol": "MARI",
      "ex_date": "2024-09-16",
      "payment_date": "2024-09-26",
      "record_date": "2024-09-18",
      "amount": 14.89,
      "year": 2024
    }
  ],
  "count": 2,
  "symbol": "MARI",
  "timestamp": 1756233106709,
  "cacheUpdated": "2025-08-26T18:16:16.816Z"
}
```

## WebSocket API

### General Information

* Connection limit: 5 connections per IP
* Subscription limit: 20 subscriptions per connection
* All messages are JSON format
* All timestamps are in Unix time format (milliseconds)

### Connection

Connect to `wss://psxterminal.com/`

**Welcome Message:**
```json
{
  "type": "welcome",
  "message": "Connected to PSX Terminal",
  "clientId": "uuid-client-id"
}
```

### Heartbeat

The server sends ping frames every 30 seconds. Clients must respond with pong frames.

**Ping Frame:**
```json
{
  "type": "ping",
  "timestamp": 1750762129000
}
```

**Pong Frame:**
```json
{
  "type": "pong",
  "timestamp": 1750762129000
}
```

### Subscription Management

#### Subscribe to Stream

**Request:**
```json
{
  "type": "subscribe",
  "subscriptionType": "marketData",
  "params": {
    "marketType": "REG"
  },
  "requestId": "req-001"
}
```

**Response:**
```json
{
  "type": "subscribeResponse",
  "requestId": "req-001",
  "status": "success",
  "subscriptionKey": "marketData:REG"
}
```

#### Unsubscribe from Stream

**Request:**
```json
{
  "type": "unsubscribe",
  "subscriptionKey": "marketData:REG",
  "requestId": "req-002"
}
```

#### List Active Subscriptions

**Request:**
```json
{
  "type": "listSubscriptions",
  "requestId": "req-003"
}
```

### Data Streams

#### Market Data Stream

Subscribe to real-time market data updates.

**Subscription Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| marketType | STRING | NO | Market filter (REG, FUT, IDX, ODL, BNB, all) |
| symbol | STRING | NO | Specific symbol filter |

**Stream Data (tickUpdate):**
```json
{
  "type": "tickUpdate",
  "symbol": "AIRLINK",
  "market": "REG",
  "tick": {
    "s": "AIRLINK",
    "m": "REG",
    "st": "OPN",
    "c": 143.05,
    "ch": 11.78,
    "pch": 0.08974,
    "v": 1279779,
    "tr": 2944,
    "val": 181562342.7,
    "h": 144,
    "l": 137.5,
    "bp": 0,
    "ap": 0,
    "bv": 0,
    "av": 0,
    "t": 1750762129000
  },
  "timestamp": 1750762129000
}
```

#### K-Line Stream

Subscribe to candlestick/kline data. Note: This is a two-step process - first request historical data, then subscribe for real-time updates.

**Step 1: Request Historical K-Lines**
```json
{
  "type": "klines",
  "symbol": "AIRLINK",
  "timeframe": "1m",
  "requestId": "req-006"
}
```

**Step 2: Subscribe for Real-time Updates**

**Subscription Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| symbol | STRING | YES | Symbol name |
| timeframe | STRING | NO | Interval (1m, 5m, 15m, 1h, 4h, 1d) |

**Stream Data:**
```json
{
  "type": "kline",
  "symbol": "AIRLINK",
  "timeframe": "1m",
  "data": [
    {
      "symbol": "AIRLINK",
      "market": "REG",
      "timestamp": 1750762129000,
      "interval": "1m",
      "open": 142.50,
      "high": 144.00,
      "low": 142.25,
      "close": 143.05,
      "volume": 1500,
      "quoteVolume": 214575.0,
      "trades": 15
    }
  ],
  "timestamp": 1750762129000
}
```

#### Statistics Stream

Subscribe to market statistics updates.

**Subscription Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| type | STRING | NO | Stats type (REG, IDX, BNB, ODL, FUT, breadth, sectors, all) |
| sector | STRING | NO | Sector filter (only with type=sectors) |

#### Symbol List Stream

Subscribe to symbol list updates.

**Stream Data:**
```json
{
  "type": "symbolList",
  "data": [
    { "symbol": "AIRLINK", "market": "REG" },
    { "symbol": "HUBC", "market": "REG" }
  ],
  "timestamp": 1750762129000
}
```

### Data Requests

#### Get Symbols

**Request:**
```json
{
  "type": "getSymbols",
  "requestId": "req-004"
}
```

#### Get Symbol Details

**Request:**
```json
{
  "type": "symbolDetails",
  "symbol": "AIRLINK",
  "requestId": "req-005"
}
```

#### Get K-Lines

**Request:**
```json
{
  "type": "klines",
  "symbol": "AIRLINK",
  "timeframe": "1m",
  "requestId": "req-006"
}
```

## Error Codes

### HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Internal Server Error |
| 503 | Service Unavailable |

### WebSocket Error Messages

```json
{
  "type": "error",
  "message": "Subscription limit exceeded",
  "requestId": "req-007",
  "timestamp": 1750762129000
}
```

## Rate Limits

* WebSocket connections: 5 per IP address
* Subscriptions: 20 per WebSocket connection
* K-line data: Maximum 100 records per request
* Message rate: No specific limit enforced

## Data Types

### Market Types

| Code | Description |
|------|-------------|
| REG | Regular Market |
| FUT | Futures |
| IDX | Indices |
| ODL | Odd Lot |
| BNB | Bills and Bonds |

### Market States

| Code | Description |
|------|-------------|
| PRE | Pre-market |
| OPN | Open |
| SUS | Suspended |
| CLS | Closed |

### Timeframes

| Code | Description |
|------|-------------|
| 1m | 1 minute |
| 5m | 5 minutes |
| 15m | 15 minutes |
| 1h | 1 hour |
| 4h | 4 hours |
| 1d | 1 day |