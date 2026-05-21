# Hybrid Automation Framework (UI + API)

## 📌 Project Description
This project is a hybrid automation testing framework combining Selenium UI testing and REST API testing using Python.

## 🚀 Features
- Selenium WebDriver (UI Automation)
- REST API Testing (requests)
- Integration Testing (API + UI)
- Page Object Model (POM)
- Pytest Framework
- Logging system
- HTML Reports
- Screenshot on failure
- Headless browser execution
- CI/CD using GitHub Actions

## 🧪 Test Scenarios
- Login functionality testing
- Add to cart functionality
- Remove from cart functionality
- Checkout flow testing
- Product API validation (GET & POST)
- API + UI integration testing

## 🛠️ Tech Stack
- Python
- Selenium
- Pytest
- Requests
- WebDriver Manager
- GitHub Actions

## ▶️ How to Run the Project

1. Install dependencies:
pip install -r requirements.txt

2. Run tests:
pytest --html=report.html

## 📂 Project Structure

```text
hybrid-automation-framework/
│
├── .github/workflows/     # GitHub Actions CI pipeline
├── api/                   # API request functions
├── assets/                # Test assets/resources
├── logs/                  # Execution logs
├── pages/                 # Page Object Model (POM) classes
├── screenshots/           # Failure screenshots
├── tests/                 # UI, API, and integration test cases
├── utils/                 # Logger and helper functions
│
├── conftest.py            # Pytest fixtures and setup
├── main.py                # Entry point (if used)
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Project dependencies
├── README.md
└── report.html            # Generated HTML report
```

## 👩‍💻 Author
Meghana D S
