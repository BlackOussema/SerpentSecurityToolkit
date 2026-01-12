# 🐍 Serpent Security Toolkit

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Type](https://img.shields.io/badge/Type-Security%20Dashboard-red.svg)

## Overview

Serpent Security Toolkit is a lightweight, open-source security auditing dashboard designed for comprehensive internal network and system analysis. It integrates essential cybersecurity functionalities, including system reconnaissance, network discovery, log analysis, and encrypted LAN messaging, all tailored for legal compliance audits and internal security assessments.

This toolkit provides a centralized platform for security professionals to gain insights into their infrastructure, identify potential vulnerabilities, and maintain a secure operational environment.

## Features

### 🔍 System Reconnaissance
*   **Hardware Information**: Gather detailed hardware specifications.
*   **Operating System Details**: Retrieve OS version, kernel info, and other relevant data.
*   **Running Processes**: Analyze active processes and their resource consumption.
*   **User Account Enumeration**: List and inspect user accounts.
*   **Installed Software**: Detect and list installed applications.

### 🌐 Network Scanner
*   **Active Host Discovery**: Identify active hosts within a specified network range.
*   **Port Scanning**: Discover open ports and services running on target hosts.
*   **Service Identification**: Determine the types and versions of services.
*   **Network Topology Mapping**: Visualize network structure.
*   **ARP Table Analysis**: Inspect ARP cache for anomalies.

### 📊 Log Analyzer
*   **System Log Parsing**: Process various system logs (e.g., syslog, auth.log).
*   **Security Event Detection**: Identify suspicious activities and security-related events.
*   **Pattern Recognition**: Detect recurring patterns that might indicate threats.
*   **Anomaly Highlighting**: Flag unusual entries for further investigation.
*   **Export Capabilities**: Export analyzed logs for external reporting.

### 💬 Encrypted LAN Messenger
*   **Secure Local Messaging**: Facilitate encrypted communication within the local network.
*   **Team Communication**: Enable secure collaboration among security teams.
*   **No External Dependencies**: Operates independently without relying on external servers.
*   **Real-time Delivery**: Ensure prompt message exchange.

### 🖥️ Web Dashboard
*   **Modern, Responsive UI**: User-friendly interface accessible from various devices.
*   **Real-time Updates**: Display live data and alerts.
*   **Interactive Visualizations**: Present complex data in an easy-to-understand graphical format.
*   **Easy Navigation**: Intuitive layout for quick access to different modules.

## Quick Start

### Prerequisites
*   Python 3.8+
*   `pip` package manager
*   Linux operating system (recommended for full functionality)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/BlackOussema/SerpentSecurityToolkit.git
    cd SerpentSecurityToolkit
    ```

2.  **Create a virtual environment (recommended)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Start the Flask server**:
    ```bash
    python src/app.py
    ```

2.  **Access the dashboard**:
    Open your web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

```
SerpentSecurityToolkit/
├── src/
│   ├── __init__.py
│   ├── app.py                 # Flask application entry point
│   ├── config.py              # Configuration settings
│   ├── dashboard/
│   │   ├── __init__.py
│   │   └── routes.py          # Dashboard routes and views
│   ├── modules/
│   │   ├── __init__.py
│   │   ├── reconnaissance.py  # System reconnaissance module
│   │   ├── network_scanner.py # Network scanning module
│   │   ├── log_analyzer.py    # Log analysis module
│   │   └── lan_messenger.py   # Encrypted LAN messaging module
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py          # Logging utilities
│   │   └── validators.py      # Input validation utilities
│   ├── templates/
│   │   ├── base.html          # Base HTML template
│   │   ├── dashboard.html     # Main dashboard view
│   │   ├── reconnaissance.html# System reconnaissance view
│   │   ├── network_scanner.html# Network scanner view
│   │   ├── log_analysis.html  # Log analysis view
│   │   └── messenger.html     # LAN messenger view
│   └── static/
│       ├── css/
│       │   └── style.css      # CSS stylesheets
│       └── js/
│           └── script.js      # JavaScript for interactivity
├── tests/
│   ├── __init__.py
│   ├── test_reconnaissance.py # Unit tests for reconnaissance
│   ├── test_network_scanner.py# Unit tests for network scanner
│   ├── test_log_analyzer.py   # Unit tests for log analyzer
│   └── test_lan_messenger.py  # Unit tests for LAN messenger
├── requirements.txt           # Python dependencies
├── LICENSE                    # Project license file
└── README.md                  # This README file
```

## Configuration

### Environment Variables

Create a `.env` file in the root directory based on `.env.example` (if provided, otherwise create one manually):

```bash
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your_strong_secret_key_here

# Network Scanner Settings
SCAN_TIMEOUT=5
MAX_THREADS=10

# Logging Settings
LOG_LEVEL=INFO
LOG_FILE=serpent.log
```

### Config File

For more advanced configurations, modify `src/config.py`:

```python
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'a_very_secret_key_for_production'
    # Add other global configurations here
    
class DevelopmentConfig(Config):
    DEBUG = True
    # Development-specific settings
    
class ProductionConfig(Config):
    DEBUG = False
    # Production-specific settings
```

## Module Usage Examples

### System Reconnaissance

```python
from src.modules.reconnaissance import SystemRecon

recon = SystemRecon()
system_info = recon.gather_info()
print(system_info)
```

### Network Scanner

```python
from src.modules.network_scanner import NetworkScanner

scanner = NetworkScanner()
hosts = scanner.discover_hosts("192.168.1.0/24")
for host in hosts:
    print(f"Found: {host}")
```

### Log Analyzer

```python
from src.modules.log_analyzer import LogAnalyzer

analyzer = LogAnalyzer("/var/log/syslog")
events = analyzer.find_security_events()
for event in events:
    print(event)
```

### LAN Messenger

```python
from src.modules.lan_messenger import LANMessenger

messenger = LANMessenger()
messenger.send("Hello, team! This is a secure message.", encrypt=True)
```

## Testing

To run the included tests:

```bash
# Install pytest if not already installed
pip install pytest pytest-cov

# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_reconnaissance.py

# Run tests with coverage report
pytest --cov=src tests/
```

## Security Considerations

### Legal Usage
*   **Authorization**: Only use this toolkit on networks and systems you own or have explicit authorization to audit.
*   **Compliance**: Ensure compliance with all applicable local, national, and international laws and regulations.
*   **Documentation**: Document all security auditing activities thoroughly.

### Best Practices
*   **Isolated Environments**: Whenever possible, run the toolkit in isolated or sandboxed environments.
*   **Strong Authentication**: Implement strong authentication mechanisms for accessing the dashboard.
*   **Regular Updates**: Keep the toolkit and its dependencies updated to the latest versions.
*   **Log Review**: Regularly review logs generated by the toolkit and the audited systems.

## Disclaimer

**This toolkit is provided for authorized security auditing and educational purposes only.**

*   Unauthorized access to computer systems is illegal and unethical.
*   The authors are not responsible for any misuse or damage caused by this toolkit.
*   Always adhere to responsible disclosure practices when identifying vulnerabilities.

## Contributing

We welcome contributions to improve Serpent Security Toolkit! Please follow these steps:

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature/YourFeature`).
3.  Implement your changes and write comprehensive tests.
4.  Ensure your code adheres to the project's coding standards.
5.  Submit a pull request with a clear description of your changes.

### Development Setup

```bash
# Install development dependencies (e.g., linters, formatters)
pip install -r requirements-dev.txt

# Run linting checks
flake8 src/

# Format code using Black
black src/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for full details.

## Author

**Ghariani Oussema**
*   GitHub: [@BlackOussema](https://github.com/BlackOussema)
*   Role: Cybersecurity Researcher & Full-Stack Developer
*   Location: Tunisia 🇹🇳

---

<p align="center">
  Made with ❤️ in Tunisia 🇹🇳
</p>
