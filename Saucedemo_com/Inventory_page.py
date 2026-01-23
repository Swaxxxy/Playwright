from playwright.sync_api import Page
import Inventory_Page_Selectors

class InventoryPage:
    def __init__(self, page:Page):
        self.page=page

        #Локаторы
        self.menu_button= page.locator(Inventory_Page_Selectors.menu_button)
        self.filter_button = page.locator(Inventory_Page_Selectors.filter_button)

        #cart
        self.cart = page.locator(Inventory_Page_Selectors.cart)
        self.cart_badge = page.locator(Inventory_Page_Selectors.cart_badge)

        #card
        self.card_header = page.locator(Inventory_Page_Selectors.card_header).first
        self.card_description = page.locator(Inventory_Page_Selectors.card_description)
        self.card_price = page.locator(Inventory_Page_Selectors.card_price)
        self.card_img = page.locator(Inventory_Page_Selectors.card_img)

        #card_button
        self.card_add_button = page.locator(Inventory_Page_Selectors.card_add_button)
        self.card_remove_button = page.locator(Inventory_Page_Selectors.card_remove_button)

        #checkout_button
        self.checkout_button = page.locator(Inventory_Page_Selectors.checkout_button)
        self.checkout_button_continue = page.locator(Inventory_Page_Selectors.checkout_button_continue)

        self.first_name_checkout = page.locator(Inventory_Page_Selectors.checkout_info_first_name)
        self.last_name_checkout = page.locator(Inventory_Page_Selectors.checkout_info_last_name)
        self.zip_code_checkout = page.locator(Inventory_Page_Selectors.checkout_info_zip_code)
        self.checkout_button_finish = page.locator(Inventory_Page_Selectors.checkout_button_finish)

        self.logo = page.locator(Inventory_Page_Selectors.logo)