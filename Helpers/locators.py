# login screen

input_field_login_username = "//input[@name='username']"
input_field_register_username = "//input[@name='email']"
input_field_login_password = "//form[@class='login']//input[@name='password']"
input_field_register_password = "//form[@class='register']//input[@name='password']"
button_login = "//form[@class='login']//input[@name='login']"
button_register = "//form[@class='register']//input[@name='register']"
error_message = "//ul[contains(@class,'error')]"
link_lost_your_password = "//a[contains(text(),'Lost')]"
checkbox_remember_me = "//input[@id='rememberme']"

# home screen

text_hello = "//p[contains(text(),'Hello')]"
button_sign_out = "//a[text()='Sign out']"
button_log_out = "//a[text()='Logout']"


# reset password screen

button_reset_password = "//input[@value='Reset Password']"


# address page

button_edit_billing_address = "//h3[contains(text(),'Billing')]/following-sibling::a[@class='edit']"
text_billing_address = "(//h3[contains(text(),'Billing')]/..)/following-sibling::address"
button_edit_shipping_address = "//h3[contains(text(),'Shipping')]/following-sibling::a[@class='edit']"
message_address_changed_successfully = "//div[@class='woocommerce-message' and contains(text(),'Address changed successfully.')]"
error_message_field_required = "//li[normalize-space()='{error_message}']"
error_box = "//ul[@class='woocommerce-error']"

input_shipping_first_name = "//input[@id='shipping_first_name']"
input_shipping_last_name = "//input[@id='shipping_last_name']"
input_shipping_company_name = "//input[@id='shipping_company']"


input_billing_first_name = "//input[@id='billing_first_name']"
input_billing_last_name = "//input[@id='billing_last_name']"
input_billing_company_name = "//input[@id='billing_company']"
input_billing_email_address = "//input[@id='billing_email']"
input_billing_phone = "//input[@id='billing_phone']"
input_billing_address_1 = "//input[@id='billing_address_1']"
input_billing_address_2 = "//input[@id='billing_address_2']"
input_billing_city = "//input[@id='billing_city']"
input_billing_postcode = "//input[@id='billing_postcode']"
dropdown_select_country_result = "//span[@class='select2-match' and text()='{country_name}']"
input_dropdown_select_country = "//input[@aria-owns='select2-results-1']"
dropdown_selected_country = "//div[contains(@class,'country_select')]/a/span"

dropdown_select_state_result = "//span[@class='select2-match' and text()='{state_name}']"
input_dropdown_select_state = "//input[@aria-owns='select2-results-2']"
dropdown_selected_state = "//div[contains(@class,'state_select')]/a/span"
input_field_state = "//input[@id='billing_state']"
button_save_address = "//input[@name='save_address']"
