Serpent Security Toolkit
Overview
The Serpent Security Toolkit is a comprehensive cybersecurity tool designed for legal internal auditing. It features a Flask web dashboard that provides functionalities
 for system reconnaissance, network scanning, log analysis, and a secure LAN messenger. This toolkit aims to assist organizations in maintaining security and compliance
  through effective internal auditing practices -//+-by Ghariani Oussema From Tunisia.

Features
System Reconnaissance:
Project Structure
SerpentSecurityToolkit
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── dashboard
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── modules
│   │   ├── __init__.py
│   │   ├── reconnaissance.py
│   │   ├── network_scanner.py
│   │   ├── log_analyzer.py
│   │   └── lan_messenger.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   └── validators.py
│   ├── templates
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── reconnaissance.html
│   │   ├── network_scanner.html
│   │   ├── log_analysis.html
│   │   └── messenger.html
│   └── static
│       ├── css
│       │   └── style.css
│       └── js
│           └── script.js
├── tests
│   ├── __init__.py
│   ├── test_reconnaissance.py
│   ├── test_network_scanner.py
│   ├── test_log_analyzer.py
│   └── test_lan_messenger.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
Installation
Clone the repository:
git clone https://github.com/BlackOussema/SerpentSecurityToolkit.git
Navigate to the project directory:
cd SerpentSecurityToolkit
Create a virtual environment:
python -m venv venv
Activate the virtual environment:
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate
Install the required dependencies:
pip install -r requirements.txt
Usage
To start the Flask application, run the following command:

python src/app.py
Access the web dashboard by navigating to http://127.0.0.1:5000 in your web browser.

Contributing
Contributions are welcome! Please refer to the CONTRIBUTING.md file for guidelines on how to contribute to this project.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
