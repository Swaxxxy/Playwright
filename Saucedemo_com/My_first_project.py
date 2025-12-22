import re
import random
import webcolors
import pytest
from datetime import datetime
from playwright.sync_api import Page,expect
project_url = 'https://www.saucedemo.com'
@pytest.fixture(autouse=True)

    # Функция для генерации текущего времени в название скриншота
def screenshot_after_test(page, request):
    yield  # сначала выполняется сам тест
    # код после теста
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    page.screenshot(path=f"screenshots/{test_name}_{timestamp}.png")

    # Функция для теста заголовка
def test_title (page:Page):
    page.goto(project_url)
    expect(page).to_have_title(re.compile('Swag Labs'))

    # Функция для теста блока авторизации - формы, содержащей поля ввода и кнопку
def test_auth_block (page:Page):
    page.goto(project_url)

    #Проверка видимости всего блока авторизации
    auth_block = page.locator('#login_button_container')
    expect(auth_block).to_be_visible()

    #Проверка видимости и плейсхолдера поля ввода Username
    username_field = page.locator('#user-name')
    expect(username_field).to_be_visible()
    expect(username_field).to_have_attribute('placeholder', 'Username')

    # Проверка видимости и плейсхолдера поля ввода Password
    password_field = page.locator('#password')
    expect(password_field).to_be_visible()
    expect(password_field).to_have_attribute('placeholder','Password')

    # Проверка видимости и названия кнопки Login
    login_button = page.locator('#login-button')
    expect(login_button).to_be_visible()
    expect(login_button).to_have_attribute('value', 'Login')

    # Функция, которая используется импортированную библиотеку webcolors для конвертации HEX в RGB
    def hex_to_rgb_str(hex_color):
        rgb = webcolors.hex_to_rgb(hex_color)
        return f"rgb({rgb.red}, {rgb.green}, {rgb.blue})"

    #Проверка цвета кнопки
    expected_color = hex_to_rgb_str("#3ddc91")  # конвертация hex → rgb
    expect(login_button).to_have_css('background-color',expected_color)

def test_futer_block (page:Page):

    page.goto(project_url)

    #Переменная для списка значений допустимых Username'ов
    cred_list_text = """Accepted usernames are:standard_userlocked_out_userproblem_userperformance_glitch_usererror_uservisual_user"""

    #Проверка наличия списка допустимых Username'ов
    cred_list = page.locator('#login_credentials')
    expect(cred_list).to_be_visible()
    expect(cred_list).to_contain_text(cred_list_text)

    #Проверка наличия допустимого пароля
    cred_passwords = page.locator('.login_password')
    expect(cred_passwords).to_be_visible()
    expect(cred_passwords).to_contain_text('Password for all users:secret_sauce')

def test_auth_blank_fields_error(page:Page):

    #Локаторы окружения
    auth_block = page.locator('#login_button_container')
    login_button = page.locator('#login-button')

    #Блок ошибок
    error_box = page.locator('.error-message-container')
    error_button = page.locator('.error-button')
    error_warning_pics = (page.locator("svg[data-icon='times-circle']")) #этот варинт использует локатор,
        # но при этом только для одного элемента,т.е проверяется только первый крестик
    # Функция, которая используется импортированную библиотеку webcolors для конвертации HEX в RGB

    def hex_to_rgb_str(hex_color):
        rgb = webcolors.hex_to_rgb(hex_color)
        return f"rgb({rgb.red}, {rgb.green}, {rgb.blue})"

    page.goto(project_url)

    # Проверка окружения - поля ввода и кнопка Login на месте
    expect(auth_block).to_be_visible()
    expect(login_button).to_be_visible()

    login_button.click()

    #Проверки после клика
    expect(error_box).to_contain_text('Epic sadface: Username is required')  # ворнинг содержит нужный тест ошибки
    expected_color = hex_to_rgb_str("#e2231a")  # конвертация hex → rgb
    expect(error_box).to_have_css('background-color', expected_color)  # ворнинг нужного цвета
    expect(error_button).to_be_visible() #ворнинг содержит крестик для закрытия
    print("count:", error_warning_pics.count())
    for i in range(error_warning_pics.count()):
        expect(error_warning_pics.nth(i)).to_be_visible() #отображаются крестики в полях ввода


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    page.screenshot(path=f"screenshots/{'after_login_click'}_{timestamp}.png")

    error_button.click()

    #Проверки после клика
    expect(error_box).to_contain_text('')  # ворнинг пустой
    expect(error_box).to_have_css('background-color', 'rgb(255, 255, 255)')
    expect(error_button).to_be_hidden()
    print("count:", error_warning_pics.count())
    for i in range(error_warning_pics.count()):
        expect(error_warning_pics.nth(i)).to_be_hidden()


def auth_invalid_field_error (page:Page):

    valid_username_list = ('standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user')
    username = random.choice(valid_username_list)

    #Селекторы:
    login_button = page.locator('#login-button')
    auth_block = page.locator('#login_button_container')
    username_field = page.locator('#user-name')
    password_field = page.locator('#password')
        # Блок ошибок
    error_box = page.locator('.error-message-container')
    error_button = page.locator('.error-button')
    error_warning_pics = (page.locator("svg[data-icon='times-circle']"))

    page.goto(project_url)

    # Проверка окружения - поля ввода и кнопка Login на месте
    expect(auth_block).to_be_visible()
    expect(login_button).to_be_visible()
    expect(username_field).to_be_visible()
    expect(password_field).to_be_visible()

    username_field.fill(username) #ввод валидного username
    login_button.click()

    #Проверки после клика
    expect(error_box).to_contain_text('Epic sadface: Username is required')  # ворнинг содержит нужный тест ошибки
    expected_color = hex_to_rgb_str("#e2231a")  # конвертация hex → rgb
    expect(error_box).to_have_css('background-color', expected_color)  # ворнинг нужного цвета
    expect(error_button).to_be_visible() #ворнинг содержит крестик для закрытия
    print("count:", error_warning_pics.count())
    for i in range(error_warning_pics.count()):
        expect(error_warning_pics.nth(i)).to_be_visible() #отображаются крестики в полях ввода


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    page.screenshot(path=f"screenshots/{'after_login_click'}_{timestamp}.png")

    error_button.click()

    #Проверки после клика
    expect(error_box).to_contain_text('')  # ворнинг пустой
    expect(error_box).to_have_css('background-color', 'rgb(255, 255, 255)')
    expect(error_button).to_be_hidden()
    print("count:", error_warning_pics.count())
    for i in range(error_warning_pics.count()):
        expect(error_warning_pics.nth(i)).to_be_hidden()







