from playwright.sync_api import Page
import Inventory_Page_Selectors

class InventoryPage:
    def __init__(self, page:Page):
        self.page=Page

        #Локаторы
        self.menu_button= page.locator(Inventory_Page_Selectors.menu_button)
        self.filter_button = page.locator(Inventory_Page_Selectors.filter_button)
        self.cart = page.locator(Inventory_Page_Selectors.cart)
        self.card_header = page.locator(Inventory_Page_Selectors.card_header)
        self.card_description = page.locator(Inventory_Page_Selectors.card_description)
        self.card_price = page.locator(Inventory_Page_Selectors.card_price)
        self.card_add_button = page.locator(Inventory_Page_Selectors.card_add_button)
        self.card_img = page.locator(Inventory_Page_Selectors.card_img)