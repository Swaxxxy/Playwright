import os
import re
import time

import pytest
import Config

from datetime import datetime
from playwright.sync_api import Page,expect
from Login_page import LoginPage
from Inventory_page import InventoryPage


@pytest.fixture() # Предусловие логина для всех тестов
def inventory(page):
    login = LoginPage(page)
    login.open()
    login.login()
    return InventoryPage(page)

@pytest.fixture(autouse=True)
def screenshot_after_test(page, request):
    yield  # сначала выполняется сам тест
    # код после теста
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    screenshots_path = os.path.join(project_root, "screenshots")
    page.screenshot(path=os.path.join(screenshots_path, f"{test_name}_{timestamp}.png"))


def test_card_transition (inventory): # тест перехода карточка - страница товара

    inventory.card_header.click()

    print("Текущий Url после перехода",inventory.page.url)
    expect(inventory.page).to_have_url('https://www.saucedemo.com/inventory-item.html?id=4')

def test_filter_work (inventory):

    # Price (Name (A to Z))
    inventory.filter_button.select_option('Name (A to Z)')
    all_headers = inventory.card_header.all_text_contents()  # получаем список всех ценников
    assert all_headers == sorted(all_headers)

    Config.take_screenshot(inventory.page,name=Config.filter_name_text_asc)

    # Price (Name (Z to A)
    inventory.filter_button.select_option('Name (Z to A)')
    all_headers = inventory.card_header.all_text_contents()  # получаем список всех ценников
    assert all_headers == sorted(all_headers,reverse=True)

    Config.take_screenshot(inventory.page,name=Config.filter_name_text_desc)

    # Price (high to low)
    inventory.filter_button.select_option('Price (high to low)')
    all_prices = inventory.card_price.all_text_contents()  # получаем список всех ценников
    all_prices = [float(price.replace('$', '')) for price in all_prices]
    assert all_prices == sorted(all_prices,reverse=True)

    Config.take_screenshot(inventory.page,name=Config.filter_name_price_desc)

    # Price (low to high)
    inventory.filter_button.select_option('Price (low to high)')
    all_prices = inventory.card_price.all_text_contents() # получаем список всех ценников
    all_prices = [float(price.replace('$','')) for price in all_prices]
    assert all_prices == sorted(all_prices)

    #Config.take_screenshot(inventory.page,name=Config.filter_name_price_asc) # фикстура сделает последний скриншот

def test_add_to_cart (inventory):

    inventory.card_add_button.click()

    #expect(inventory.card_add_button).to_have_attribute()
    expect(inventory.cart_badge).to_contain_text("1")

    time.sleep(1) #пауза для отрисовки изображений и иконок
    Config.take_screenshot(inventory.page, name="1 item Added")

    inventory.card_remove_button.click()

    expect(inventory.cart_badge).not_to_be_visible()