from playwright.sync_api import Page
import Login_Page_Selectors

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        #Локаторы
        self.auth_block = page.locator(Login_Page_Selectors.auth_block)
        self.username_field = page.locator(Login_Page_Selectors.username_field)
        self.password_field = page.locator(Login_Page_Selectors.password_field)
        self.login_button = page.locator(Login_Page_Selectors.login_button)
        self.cred_list = page.locator(Login_Page_Selectors.cred_list)
        self.error_box = page.locator(Login_Page_Selectors.error_box)
        self.error_button = page.locator(Login_Page_Selectors.error_button)
        self.error_warning_pics = page.locator(Login_Page_Selectors.error_warning_pics)
        self.cred_passwords = page.locator(Login_Page_Selectors.cred_passwords)