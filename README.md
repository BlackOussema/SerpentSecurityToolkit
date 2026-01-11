<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Flask-2.0+-green.svg" alt="Flask">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Type-Security%20Dashboard-red.svg" alt="Type">
</p>

<h1 align="center">🐍 Serpent Security Toolkit</h1>

<p align="center">
  <strong>Comprehensive Security Auditing Dashboard</strong>
</p>

<p align="center">
  A lightweight, open-source security auditing dashboard for internal network<br>
  and system analysis. Features system reconnaissance, network discovery,<br>
  log analysis, and encrypted LAN messaging.
</p>

---

## ✨ Features

### 🔍 System Reconnaissance
- Hardware information gathering
- Operating system details
- Running processes analysis
- User account enumeration
- Installed software detection

### 🌐 Network Scanner
- Active host discovery
- Port scanning
- Service identification
- Network topology mapping
- ARP table analysis

### 📊 Log Analyzer
- System log parsing
- Security event detection
- Pattern recognition
- Anomaly highlighting
- Export capabilities

### 💬 LAN Messenger
- Encrypted local messaging
- Secure team communication
- No external dependencies
- Real-time delivery

### 🖥️ Web Dashboard
- Modern, responsive UI
- Real-time updates
- Interactive visualizations
- Easy navigation

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Linux operating system (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/BlackOussema/SerpentSecurityToolkit.git
cd SerpentSecurityToolkit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Start the Flask server
python src/app.py

# Access the dashboard
# Open http://127.0.0.1:5000 in your browser
```

---

## 📁 Project Structure

```
SerpentSecurityToolkit/
├── src/
│   ├── __init__.py
│   ├── app.py                 # Flask application entry
│   ├── config.py              # Configuration settings
│   ├── dashboard/
│   │   ├── __init__.py
│   │   └── routes.py          # Dashboard routes
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── reconnaissance.py  # System recon module
│   │   ├── network_scanner.py # Network scanning
│   │   ├── log_analyzer.py    # Log analysis
│   │   └── lan_messenger.py   # Encrypted messaging
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py          # Logging utilities
│   │   └── validators.py      # Input validation
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── reconnaissance.html
│   │   ├── network_scanner.html
│   │   ├── log_analysis.html
│   │   └── messenger.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── script.js
├── tests/
│   ├── __init__.py
│   ├── test_reconnaissance.py
│   ├── test_network_scanner.py
│   ├── test_log_analyzer.py
│   └── test_lan_messenger.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```bash
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here

# Network Scanner
SCAN_TIMEOUT=5
MAX_THREADS=10

# Logging
LOG_LEVEL=INFO
LOG_FILE=serpent.log
```

### Config File

Edit `src/config.py` for advanced settings:

```python
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your-secret-key'
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False
```

---

## 📖 Module Documentation

### System Reconnaissance

```python
from modules.reconnaissance import SystemRecon

recon = SystemRecon()
system_info = recon.gather_info()
print(system_info)
```

### Network Scanner

```python
from modules.network_scanner import NetworkScanner

scanner = NetworkScanner()
hosts = scanner.discover_hosts("192.168.1.0/24")
for host in hosts:
    print(f"Found: {host}")
```

### Log Analyzer

```python
from modules.log_analyzer import LogAnalyzer

analyzer = LogAnalyzer("/var/log/syslog")
events = analyzer.find_security_events()
```

### LAN Messenger

```python
from modules.lan_messenger import LANMessenger

messenger = LANMessenger()
messenger.send("Hello, team!", encrypt=True)
```

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run specific test
pytest tests/test_reconnaissance.py

# Run with coverage
pytest --cov=src tests/
```

---

## 📋 Requirements

```
Flask>=2.0.0
python-dotenv>=0.19.0
psutil>=5.8.0
netifaces>=0.11.0
cryptography>=3.4.0
scapy>=2.4.5
```

---

## 🔒 Security Considerations

### Legal Usage
- Only use on networks you own or have authorization to audit
- Comply with all applicable laws and regulations
- Document all testing activities

### Best Practices
- Run in isolated environments when possible
- Use strong authentication
- Keep the toolkit updated
- Review logs regularly

---

## 🖼️ Screenshots

### Dashboard
The main dashboard provides an overview of system health and recent activities.

### Network Scanner
Visual representation of discovered hosts and open ports.

### Log Analysis
Interactive log viewer with filtering and search capabilities.

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Write tests for new features
4. Submit a pull request

### Development Setup

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run linting
flake8 src/

# Format code
black src/
```

---

## ⚠️ Disclaimer

**This toolkit is for authorized security auditing only.**

- Only use on systems you own or have explicit permission to test
- Unauthorized access to computer systems is illegal
- The authors are not responsible for misuse
- Always follow responsible disclosure practices

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ghariani Oussema**
- GitHub: [@BlackOussema](https://github.com/BlackOussema)
- Role: Cyber Security Researcher & Full-Stack Developer
- Location: Tunisia 🇹🇳

---

<p align="center">
  Made with ❤️ in Tunisia 🇹🇳
</p>
