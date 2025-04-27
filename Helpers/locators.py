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
text_shipping_address = "(//h3[contains(text(),'Shipping')]/..)/following-sibling::address"
button_edit_shipping_address = "//h3[contains(text(),'Shipping')]/following-sibling::a[@class='edit']"
message_address_changed_successfully = "//div[@class='woocommerce-message' and contains(text(),'Address changed successfully.')]"
error_message_field_required = "//li[normalize-space()='{error_message}']"
error_box = "//ul[@class='woocommerce-error']"

input_shipping_first_name = "//input[@id='shipping_first_name']"
input_shipping_last_name = "//input[@id='shipping_last_name']"
input_shipping_company_name = "//input[@id='shipping_company']"
input_shipping_address_1 = "//input[@id='shipping_address_1']"
input_shipping_address_2 = "//input[@id='shipping_address_2']"
input_shipping_city = "//input[@id='shipping_city']"
input_shipping_postcode = "//input[@id='shipping_postcode']"

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
input_field_billing_state = "//input[@id='billing_state']"
input_field_shipping_state = "//input[@id='shipping_state']"
button_save_address = "//input[@name='save_address']"


# shop page

shop_link = "//a[text()='Shop']"

items_in_shop = "//ul[contains(@class,'products')]//li"
item_names = "(//ul[contains(@class,'products')]//li//h3)[{item_num}]"
item_prices = "((//ul[contains(@class,'products')]//span[@class='price'])[{item_num}]//span[contains(@class,'amount')])[last()]"

cart_amount = "(//a[@title='View your shopping cart']//span)[last()]"
number_of_items_in_cart = "//span[@class='cartcontents']"
button_add_to_cart = "(//a[contains(@class,'add_to_cart')])[{item_num}]"
current_cart_count = "//span[@class='cartcontents' and contains(text(),'{item_num}')]"


# cart page

button_remove_item_from_cart = "//td[@class='product-remove']//a"
product_name_on_cart_page = "(//td[@class='product-name'])[{item_num}]"
product_price_on_cart_page = "(//td[@class='product-price'])[{item_num}]"
product_quantity_on_cart_page = "(//td[@class='product-quantity']//input)[{item_num}]"
empty_cart_message = "//p[@class='cart-empty']"