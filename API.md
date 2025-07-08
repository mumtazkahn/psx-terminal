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

#### Market Data
```
GET /api/market-data
```
Get market data for all symbols or filtered by market type.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| market | STRING | NO | Market filter (REG, FUT, IDX, ODL, BNB) |

**Response:**
```json
{
  "success": true,
  "data": {
    "REG": {
      "AIRLINK": {
        "market": "REG",
        "st": "OPN",
        "symbol": "AIRLINK",
        "price": 143.05,
        "change": 11.78,
        "changePercent": 0.08974,
        "volume": 1279779,
        "trades": 2944,
        "value": 181562342.7,
        "high": 144,
        "low": 137.5,
        "bid": 0,
        "ask": 0,
        "bidVol": 0,
        "askVol": 0,
        "timestamp": 1750762129
      }
    }
  },
  "timestamp": 1750762129
}
```

#### Market Statistics
```
GET /api/stats
```
Get market statistics and breadth indicators.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| type | STRING | NO | Stats type (REG, IDX, BNB, ODL, FUT, breadth, sectors) |

**Response (all stats):**
```json
{
  "success": true,
  "data": {
    "REG": {
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
    "breadth": {
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
    "sectors": {
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
    }
  },
  "timestamp": 1750762129
}
```

**Response (specific type, e.g. `?type=breadth`):**
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

#### Symbol List
```
GET /api/symbols
```
Get all available trading symbols.

**Response:**
```json
{
  "success": true,
  "data": [
    { "symbol": "AIRLINK", "market": "REG" },
    { "symbol": "HUBC", "market": "REG" },
    { "symbol": "NML-AUG", "market": "FUT" }
  ],
  "timestamp": 1750762129
}
```

#### Symbol Yields
```
GET /api/yields/{symbol}
```
Get yield metrics and financial ratios for a specific symbol.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| symbol | STRING | YES | Symbol name (e.g., SSGC) |

**Response:**
```json
{
  "success": true,
  "data": {
    "symbol": "SSGC",
    "sector": "0821",
    "listedIn": "ALLSHR,JSMFI,KMIALLSHR",
    "marketCap": "41.0B",
    "price": 46.53,
    "changePercent": 1.262,
    "yearChange": 374.795918367347,
    "peRatio": 5.4294049008168,
    "dividendYield": 0,
    "freeFloat": "308.3M",
    "volume30Avg": 26831414.5,
    "isNonCompliant": false,
    "timestamp": "2025-07-08T14:35:52.887Z"
  },
  "timestamp": 1751988094625
}
```

#### Company Information
```
GET /api/company/{symbol}
```
Get detailed company information including financial stats and business description.

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| symbol | STRING | YES | Symbol name (e.g., SSGC) |

**Response:**
```json
{
  "success": true,
  "data": {
    "symbol": "SSGC",
    "scrapedAt": "2025-06-26T19:06:00.398Z",
    "financialStats": {
      "marketCap": {
        "raw": "37,412,515.64",
        "numeric": 37412515.64
      },
      "shares": {
        "raw": "880,916,309",
        "numeric": 880916309
      },
      "freeFloat": {
        "raw": "308,320,708",
        "numeric": 308320708
      },
      "freeFloatPercent": {
        "raw": "35.00%",
        "numeric": 35
      }
    },
    "businessDescription": "Sui Southern Gas Company Limited's main activity is transmission and distribution of natural gas in Sindh and Baluchistan. The Company is also engaged in certain activities related to the gas business including the manufacturing and sale of gas meters and construction contracts for laying of pipelines.",
    "keyPeople": [
      {
        "name": "Muhammad Amin Rajput (Acting)",
        "position": "CEO"
      },
      {
        "name": "Dr. Shamshad Akhtar",
        "position": "Chairperson"
      },
      {
        "name": "Fawad Ahmed Khan",
        "position": "Company Secretary"
      }
    ],
    "error": null
  },
  "timestamp": 1751988182467
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