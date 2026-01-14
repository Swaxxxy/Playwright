import os
import pytest

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

