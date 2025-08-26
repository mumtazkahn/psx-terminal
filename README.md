# PSX Terminal

<div align="center">

![PSX Terminal](https://img.shields.io/badge/PSX-Terminal-yellow?style=for-the-badge)

[![Version](https://img.shields.io/badge/version-1.1.0-blue)](https://github.com/mumtazkahn/psx-terminal)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![API](https://img.shields.io/badge/API-documented-blue)](API.md)
[![Live](https://img.shields.io/badge/live-psxterminal.com-success)](https://psxterminal.com)

**Professional Real-time Market Data Platform for Pakistan Stock Exchange**

*Modern web-based terminal for live market monitoring, data visualization, and comprehensive market analysis*

[🌐 Live Platform](https://psxterminal.com) • [📚 API Docs](API.md) • [🏗️ Architecture](ARCHITECTURE.md) • [💻 Examples](examples/) • [📸 Screenshots](screenshots/)

</div>

---

## 📊 Performance Metrics

<div align="center">

| Metric | Value | Description |
|--------|-------|-------------|
| **Latency** | Real-time | Live data delivery |
| **Uptime** | High | Production reliability |
| **Symbols** | Comprehensive | Market coverage |
| **Updates/sec** | 100/sec | Real-time throughput |

</div>

---

## ⚡ Quick Start

### Try the Platform
1. **Visit** [psxterminal.com](https://psxterminal.com)
2. **Explore** real-time market data
3. **Test** WebSocket API
4. **Check** documentation

### Integrate Our API
```bash
# Get live market data for a symbol
curl "https://psxterminal.com/api/ticks/REG/HUBC"

# Get market statistics
curl "https://psxterminal.com/api/stats/REG"

# Get dividend history
curl "https://psxterminal.com/api/dividends/MARI"
```

### For Developers
- 📖 [API Documentation](API.md)
- 💻 [Integration Examples](examples/)
- 🏗️ [Architecture](ARCHITECTURE.md)

---

## ✨ Features

### 📈 Real-time Market Data
- **Live price updates** across all PSX markets (REGULAR, FUTURES, Indices, ODD Lot, BILLS and BONDS)
- **Real-time charts** with multiple timeframes (1m, 5m, 15m, 1h, 4h, 1d)
- **Market breadth indicators** showing advances vs declines
- **Instant tick-by-tick** price streaming

### 📊 Professional Interface
- **Interactive candlestick charts** with multiple timeframes
- **Customizable watchlists** and monitoring dashboards
- **Sector analysis** with performance metrics
- **Advanced filtering** and search capabilities
- **Dark/Light theme** with responsive design
- **Progressive Web App** for seamless mobile experience

### 🔍 Analysis Tools
- **Top gainers and losers** monitoring
- **Volume and value** analysis
- **Sector performance** breakdown
- **Market statistics** and breadth indicators
- **Symbol lookup** with detailed data
- **Real-time news and announcements** for market insights
- **Deep financial analysis** with comprehensive fundamentals

### 🛠️ Developer APIs
- **RESTful APIs** for market data access
- **WebSocket streaming** for real-time updates
- **Comprehensive documentation** with examples
- **Rate limiting** and usage guidelines

---

## 📸 Platform Preview

<div align="center">

### Home
<img src="screenshots/home.jpg" width="300" alt="Home">

### Market
<img src="screenshots/market.jpg" width="300" alt="Market">

### Charts
<img src="screenshots/charts.jpg" width="300" alt="Charts">

### Fundamentals
<img src="screenshots/fundamentals.jpg" width="300" alt="Fundamentals">

### PE Yields
<img src="screenshots/PE-Yields.jpg" width="300" alt="PE Yields">

### Dividends History
<img src="screenshots/dividends_history.jpg" width="300" alt="Dividends History">

### App
<img src="screenshots/App.jpg" width="300" alt="App">

*[View all screenshots →](screenshots/)*

</div>

---

## 🚀 Technology Stack

### Frontend
- **SvelteKit** - Server-side rendering with optimal performance
- **TailwindCSS** - Utility-first responsive design system
- **Lightweight Charts** - Financial charting optimized for real-time data
- **Progressive Web App** - Native app-like experience

### Backend
- **Node.js** - Event-driven runtime for high concurrency
- **Express.js** - Minimalist web framework
- **WebSocket** - Real-time data streaming
- **PostgreSQL** - ACID-compliant data persistence
- **Redis** - High-performance caching and session management

---

## 📱 Platform Access

### Web Application
Visit **[psxterminal.com](https://psxterminal.com)** for full market monitoring:
- Real-time dashboard with live updates
- Interactive charts with multiple timeframes
- Customizable watchlists and tools
- Sector performance tracking
- Real-time news and announcements
- Deep financial analysis and fundamentals
- Mobile-optimized responsive interface
- Progressive Web App functionality

### API Access
Integrate PSX data into your applications:
- **REST API** for market data queries
- **WebSocket API** for live streaming
- **Comprehensive documentation** with examples

---

## 📊 Market Coverage

| Market | Description | Coverage | Real-time |
|--------|-------------|----------|-----------|
| **REGULAR** | Regular Market | Listed companies | ✅ |
| **FUTURES** | Futures | Commodity/index futures | ✅ |
| **Indices** | Indices | KSE-100, KSE-30, sectors | ✅ |
| **ODD Lot** | Odd Lot | Fractional shares | ✅ |
| **BILLS and BONDS** | Bills and Bonds | Government/corporate | ✅ |

---

## 🔌 API Examples

### REST API
```bash
# Get single symbol market data
curl "https://psxterminal.com/api/ticks/REG/HUBC"

# Get all available symbols
curl "https://psxterminal.com/api/symbols"

# Get market statistics
curl "https://psxterminal.com/api/stats/REG"

# Get company information
curl "https://psxterminal.com/api/companies/HUBC"

# Get fundamental analysis
curl "https://psxterminal.com/api/fundamentals/HUBC"

# Get dividend history
curl "https://psxterminal.com/api/dividends/MARI"

# Get historical kline data
curl "https://psxterminal.com/api/klines/HUBC/1h?limit=50"
```

### WebSocket
```javascript
import WebSocket from 'ws';

// Connect and subscribe
const ws = new WebSocket('wss://psxterminal.com/');

// Wait for connection to open
ws.onopen = () => {
  console.log('Connected!');
  ws.send(JSON.stringify({
    type: 'subscribe',
    subscriptionType: 'marketData',
    params: { marketType: 'REG' }
  }));
};

// Handle updates
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  console.log('Market update:', data);
};

// Handle errors
ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};

// Handle close
ws.onclose = () => {
  console.log('Connection closed');
};
```



*[Complete examples →](examples/)*

---

## 📚 Documentation

| Resource | Description |
|----------|-------------|
| [📖 API Reference](API.md) | Complete REST and WebSocket documentation |
| [🏗️ Architecture](ARCHITECTURE.md) | System design and technical overview |
| [💻 Examples](examples/) | Integration examples and code samples |
| [📸 Screenshots](screenshots/) | Platform interface demonstrations |
| [📋 Changelog](CHANGELOG.md) | Version history and updates |
| [🔒 Security](SECURITY.md) | Security policy and reporting |
| [🤝 Contributing](CONTRIBUTING.md) | Development and contribution guidelines |

---

## 👥 Community & Support

### Getting Help
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/mumtazkahn/psx-terminal/issues)
- 💡 **Feature Requests**: [GitHub Discussions](https://github.com/mumtazkahn/psx-terminal/discussions)
- 📖 **Documentation**: [API Reference](API.md)
- 🌐 **Live Platform**: [psxterminal.com](https://psxterminal.com)

### Contributing
See [Contributing Guide](CONTRIBUTING.md) for:
- Development setup
- Code standards
- Pull request process



---

## 🌟 Key Highlights

### Performance
- **Real-time** data updates and streaming
- **High throughput** concurrent processing
- **Reliable** uptime and stability
- **Cross-platform** compatibility

### User Experience
- **Intuitive interface** for efficient monitoring
- **Mobile-optimized** responsive design
- **Progressive Web App** for native experience
- **Customizable dashboards** and preferences
- **Comprehensive search** and filtering

### Developer Experience
- **Complete API documentation** with examples
- **Multiple integration options** (REST/WebSocket)
- **Open source** with active community
- **Modern technology stack**

---

## 📈 Roadmap

### Current ✅
- [x] Real-time market data streaming
- [x] Professional monitoring interface
- [x] Interactive candlestick charts
- [x] Market analysis tools
- [x] RESTful and WebSocket APIs
- [x] Mobile-optimized design
- [x] Dark/Light theme support
- [x] Progressive Web App (PWA)
- [x] Real-time news and announcements
- [x] Deep financial analysis with fundamentals
- [x] Historical dividend data

### Upcoming 🚧
- [ ] **Mobile Apps** (iOS/Android)
- [ ] **Advanced Analytics** (Technical indicators)
- [ ] **Portfolio Tools** (Tracking, analysis)
- [ ] **Alert System** (Email/SMS notifications)
- [ ] **Market Scanner** (Custom screening)
- [ ] **Historical Data** (Extended analysis)

### Future 🔮
- [ ] **AI-Powered Insights** (Sentiment analysis)
- [ ] **Social Features** (Community, shared lists)
- [ ] **Advanced Charting** (Drawing tools)
- [ ] **Institution Features** (Multi-user accounts)

---

## 🏆 Recognition

### Production Ready
- **Live platform** at [psxterminal.com](https://psxterminal.com)
- **Stable API** with consistent performance
- **Professional infrastructure** and monitoring

### Community Impact
- **Open source** contribution to Pakistani fintech
- **Developer friendly** comprehensive documentation
- **Educational resource** for financial technology

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

<div align="center">

### 🚀 Ready to Get Started?

**[Explore Live Platform](https://psxterminal.com)** • **[Read API Docs](API.md)** • **[View Examples](examples/)**

**Built for Pakistani fintech community • Open source • Production ready**

⭐ **Star this repo if it's useful!** ⭐

---

**PSX Terminal** - *Professional market data platform by developers, for developers*

</div>