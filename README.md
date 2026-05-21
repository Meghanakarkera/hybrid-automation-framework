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
pytest

3. Generate HTML Report
pytest --html=report.html

## 📂 Project Structure
hybrid-automation-framework/
│
├── tests/           # UI, API, and integration test cases
├── pages/           # Page Object Model (POM) classes
├── api/             # API request functions
├── utils/           # Logger and utility/helper functions
├── logs/            # Execution logs
├── screenshots/    # Failure screenshots
├── reports/         # HTML test reports
├── .github/workflows/   # GitHub Actions CI pipeline
├── requirements.txt
├── pytest.ini
└── README.md

## 👩‍💻 Author
Meghana D S
