This repository contains automated test cases for the website https://practice.automationtesting.in/,
created using Selenium and pytest frameworks.

📋 Prerequisites
1. Python 3.7 or above installed
2. pip installed (Python package manager)
3. Chrome browser installed (or modify the driver settings accordingly)

📦 Setup Instructions
1. Clone the repository using command: git clone https://github.com/Anshul-Bidhuri/automationtesting.in.git
2. Navigate to the project directory
3. Create a virtual environment using command: python -m venv venv
4. Activate the virtual environment using command: source venv/bin/activate (for Mac) or venv/Scripts/activate (for Windows)
5. Install the dependencies using command: pip install -r requirements.txt
6. Run the test cases using command: pytest --html=AutomationAssignment.html --self-contained-html --disable-warnings

The run command will also generate an HTML report named AutomationAssignment.html after the test execution.


🏷️ Test Organization with Markers

To organize the test cases better, we use the following pytest markers:

    login_user: Login user test cases.
    register_user: Register user test cases.
    billing_address_page: Billing address test cases.
    shipping_address_page: Shipping address test cases.
    positive_cases: positive flow cases.

Example 1: Run only login user and positive test cases:

    pytest --html=AutomationAssignment.html --self-contained-html --disable-warnings -m "login_user and positive_cases"

Example 2: Run only the negative test cases of the billing address page:

    pytest --html=AutomationAssignment.html --self-contained-html --disable-warnings -m "billing_address_page and not positive_cases"


🚀 Happy Testing!
