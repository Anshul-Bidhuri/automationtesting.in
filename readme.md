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
    shop_page_cases: shop page test cases.

Example 1: Run only login user and positive test cases:

    pytest --html=AutomationAssignment.html --self-contained-html --disable-warnings -m "login_user and positive_cases"

Example 2: Run only the negative test cases of the billing address page:

    pytest --html=AutomationAssignment.html --self-contained-html --disable-warnings -m "billing_address_page and not positive_cases"


## 🧪 Automated Test Cases

### Register New User (`tests/test_register_new_user.py`)
- **test_register_with_empty_email_and_password**  
  Verifies registration fails when both email and password are empty.
- **test_register_with_valid_email_and_empty_password**  
  Checks registration with a valid email but empty password.
- **test_register_with_empty_email_and_valid_password**  
  Checks registration with an empty email but valid password.
- **test_register_with_invalid_email_format**  
  Ensures error is shown for invalid email format.
- **test_register_with_weak_password**  
  Ensures error is shown for weak password.
- **test_register_with_already_registered_email**  
  Ensures error is shown for an already registered email.
- **test_register_with_javascript_email_and_valid_password**  
  Checks for script injection in the email field.
- **test_register_with_valid_new_email_and_password**  
  Verifies successful registration with valid new credentials.

### Login User (`tests/test_login_user.py`)
- **test_login_with_empty_email_and_password**  
  Verifies login fails with both fields empty.
- **test_login_with_valid_email_and_empty_password**  
  Checks login with valid email but empty password.
- **test_login_with_empty_email_and_valid_password**  
  Checks login with empty email but valid password.
- **test_login_with_wrong_password**  
  Ensures error is shown for incorrect password.
- **test_login_with_old_valid_credentials**  
  Verifies login with existing valid credentials.
- **test_login_with_new_registered_credentials**  
  Verifies login with newly registered credentials.
- **test_login_page_remember_me_checkbox**  
  Checks the functionality of the "Remember Me" checkbox.
- **test_login_page_lost_your_password_link**  
  Verifies the "Lost your password" link displays the reset password option.
- **test_register_with_javascript_email_and_valid_password**  
  Checks for script injection in the email field during login.

### Billing Address Page (`tests/test_billing_address_page.py`)

- **test_complete_edit_billing_address**  
  Verifies user can complete and save billing address with all valid data.
- **test_complete_edit_billing_address_without_mandatory_fields**  
  Checks that the billing address can be saved when optional fields are left empty.
- **test_save_billing_address_first_name_field_min_length_check**  
  Ensures an error is shown if the first name is shorter than the minimum allowed length.
- **test_save_billing_address_with_empty_first_name_field**  
  Ensures an error is displayed when the first name field is left empty.
- **test_save_billing_address_with_invalid_first_name_field**  
  Ensures an error is shown if the first name contains special characters.
- **test_save_billing_address_with_javascript_code_inside_first_name_field**  
  Ensures an error is shown if the first name contains JavaScript code (script injection).
- **test_save_billing_address_last_name_field_min_length_check**  
  Ensures an error is shown if the last name is shorter than the minimum allowed length.
- **test_save_billing_address_with_empty_last_name_field**  
  Ensures an error is displayed when the last name field is left empty.
- **test_save_billing_address_with_invalid_last_name_field**  
  Ensures an error is shown if the last name contains special characters.
- **test_save_billing_address_with_javascript_code_inside_last_name_field**  
  Ensures an error is shown if the last name contains JavaScript code (script injection).
- **test_save_billing_address_with_empty_email_field**  
  Ensures an error is displayed when the email field is left empty.
- **test_save_billing_address_with_invalid_email_format**  
  Ensures an error appears for invalid email formats.
- **test_save_billing_address_with_javascript_code_inside_email_field**  
  Ensures an error is shown if the email field contains JavaScript code (script injection).
- **test_save_billing_address_with_javascript_code_inside_company_name_field**  
  Ensures an error is shown if the company name contains JavaScript code (script injection).
- **test_save_billing_address_with_invalid_char_inside_company_name_field**  
  Ensures an error is shown if the company name contains special characters.
- **test_save_billing_address_with_empty_phone_field**  
  Ensures an error is displayed when the phone field is left empty.
- **test_save_billing_address_with_invalid_phone_format**  
  Ensures an error for phone numbers that are too short or not valid.
- **test_save_billing_address_with_max_length_phone_check**  
  Ensures an error for phone numbers that are too long.
- **test_save_billing_address_with_javascript_code_inside_phone_field**  
  Ensures an error is shown if the phone field contains JavaScript code (script injection).
- **test_save_billing_address_with_string_inside_phone_field**  
  Ensures an error is shown if the phone field contains alphabetic characters.
- **test_save_billing_address_with_empty_address_1_field**  
  Ensures an error is displayed when Address Line 1 is left empty.
- **test_save_billing_address_with_invalid_address_1_format**  
  Ensures an error for invalid Address Line 1 format (e.g., special characters).
- **test_save_billing_address_with_min_length_address_1_check**  
  Ensures an error is shown if Address Line 1 is too short.
- **test_save_billing_address_with_javascript_code_inside_address_1_field**  
  Ensures an error is shown if Address Line 1 contains JavaScript code.
- **test_save_billing_address_with_javascript_code_inside_address_2_field**  
  Ensures an error is shown if Address Line 2 contains JavaScript code.
- **test_save_billing_address_with_invalid_char_inside_address_2_field**  
  Ensures an error is shown if Address Line 2 contains special characters.
- **test_save_billing_address_with_empty_city_field**  
  Ensures an error is displayed when the city field is left empty.
- **test_save_billing_address_with_invalid_city_format**  
  Ensures an error for invalid city format (e.g., special characters).
- **test_save_billing_address_with_min_length_city_check**  
  Ensures an error is shown if the city name is too short.
- **test_save_billing_address_with_javascript_code_inside_city_field**  
  Ensures an error is shown if the city field contains JavaScript code.
- **test_save_billing_address_with_empty_postcode_field**  
  Ensures an error is displayed when the postcode field is left empty.
- **test_save_billing_address_with_invalid_postcode_format**  
  Ensures an error for invalid postcode format (e.g., too short).
- **test_save_billing_address_with_max_length_postcode_check**  
  Ensures an error for postcode values that are too long.
- **test_save_billing_address_with_javascript_code_inside_postcode_field**  
  Ensures an error is shown if the postcode field contains JavaScript code.
- **test_save_billing_address_with_string_inside_postcode_field**  
  Ensures an error is shown if the postcode field contains alphabetic characters.
- **test_billing_address_country_dropdown**  
  Verifies that the country dropdown allows selection and saves the correct country.
- **test_billing_address_state_dropdown**  
  Verifies that the state dropdown allows selection and saves the correct state.

### Shipping Address Page (`tests/test_shipping_adress_page.py`)

- **test_complete_edit_shipping_address**  
  Verifies user can complete and save shipping address with all valid data.
- **test_complete_edit_shipping_address_without_mandatory_fields**  
  Checks that the shipping address can be saved when optional fields are left empty.
- **test_save_shipping_address_first_name_field_min_length_check**  
  Ensures an error is shown if the first name is shorter than the minimum allowed length.
- **test_save_shipping_address_with_empty_first_name_field**  
  Ensures an error is displayed when the first name field is left empty.
- **test_save_shipping_address_with_invalid_first_name_field**  
  Ensures an error is shown if the first name contains special characters.
- **test_save_shipping_address_with_javascript_code_inside_first_name_field**  
  Ensures an error is shown if the first name contains JavaScript code (script injection).
- **test_save_shipping_address_last_name_field_min_length_check**  
  Ensures an error is shown if the last name is shorter than the minimum allowed length.
- **test_save_shipping_address_with_empty_last_name_field**  
  Ensures an error is displayed when the last name field is left empty.
- **test_save_shipping_address_with_invalid_last_name_field**  
  Ensures an error is shown if the last name contains special characters.
- **test_save_shipping_address_with_javascript_code_inside_last_name_field**  
  Ensures an error is shown if the last name contains JavaScript code (script injection).
- **test_save_shipping_address_with_javascript_code_inside_company_name_field**  
  Ensures an error is shown if the company name contains JavaScript code (script injection).
- **test_save_shipping_address_with_invalid_char_inside_company_name_field**  
  Ensures an error is shown if the company name contains special characters.
- **test_save_shipping_address_with_empty_address_1_field**  
  Ensures an error is displayed when Address Line 1 is left empty.
- **test_save_shipping_address_with_invalid_address_1_format**  
  Ensures an error for invalid Address Line 1 format (e.g., special characters).
- **test_save_shipping_address_with_min_length_address_1_check**  
  Ensures an error is shown if Address Line 1 is too short.
- **test_save_shipping_address_with_javascript_code_inside_address_1_field**  
  Ensures an error is shown if Address Line 1 contains JavaScript code.
- **test_save_shipping_address_with_javascript_code_inside_address_2_field**  
  Ensures an error is shown if Address Line 2 contains JavaScript code.
- **test_save_shipping_address_with_invalid_char_inside_address_2_field**  
  Ensures an error is shown if Address Line 2 contains special characters.
- **test_save_shipping_address_with_empty_city_field**  
  Ensures an error is displayed when the city field is left empty.
- **test_save_shipping_address_with_invalid_city_format**  
  Ensures an error for invalid city format (e.g., special characters).
- **test_save_shipping_address_with_min_length_city_check**  
  Ensures an error is shown if the city name is too short.
- **test_save_shipping_address_with_javascript_code_inside_city_field**  
  Ensures an error is shown if the city field contains JavaScript code.
- **test_save_shipping_address_with_empty_postcode_field**  
  Ensures an error is displayed when the postcode field is left empty.
- **test_save_shipping_address_with_invalid_postcode_format**  
  Ensures an error for invalid postcode format (e.g., too short).
- **test_save_shipping_address_with_max_length_postcode_check**  
  Ensures an error for postcode values that are too long.
- **test_save_shipping_address_with_javascript_code_inside_postcode_field**  
  Ensures an error is shown if the postcode field contains JavaScript code.
- **test_save_shipping_address_with_string_inside_postcode_field**  
  Ensures an error is shown if the postcode field contains alphabetic characters.
- **test_shipping_address_country_dropdown**  
  Verifies that the country dropdown allows selection and saves the correct country.
- **test_shipping_address_state_dropdown**  
  Verifies that the state dropdown allows selection and saves the correct state.

### 5. Shop Page (`tests/test_add_remove_products_to_cart.py`)
- **test_total_price_after_updating_the_cart**  
  Verifies that the total cart price updates correctly after changing item quantities.

🚀 Happy Testing!