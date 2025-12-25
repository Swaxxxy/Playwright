import re
import pytest

from Config import project_url,project_url_after_auth,cred_list_text,hex_to_rgb_str
from datetime import datetime
from playwright.sync_api import Page,expect
from Login_page import LoginPage

@pytest.fixture
def login(page):
    return LoginPage(page)

@pytest.fixture(autouse=True)
    #Функция для генерации текущего времени в название скриншота
def screenshot_after_test(page, request):
    yield  # сначала выполняется сам тест
    # код после теста
    test_name = request.node.name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    page.screenshot(path=f"screenshots/{test_name}_{timestamp}.png")

    #Функция для теста заголовка
def test_title (login):
    login.page.goto(project_url)
    expect(login.page).to_have_title(re.compile('Swag Labs'))

    #Функция для теста блока авторизации - формы, содержащей поля ввода и кнопку
def test_auth_block (login):

    login.page.goto(project_url)

    #Проверка видимости всего блока авторизации
    expect(login.auth_block).to_be_visible()

    #Проверка видимости и плейсхолдера поля ввода Username
    expect(login.username_field).to_be_visible()
    expect(login.username_field).to_have_attribute('placeholder', 'Username')

    #Проверка видимости и плейсхолдера поля ввода Password
    expect(login.password_field).to_be_visible()
    expect(login.password_field).to_have_attribute('placeholder','Password')

    #Проверка видимости и названия кнопки Login
    expect(login.login_button).to_be_visible()
    expect(login.login_button).to_have_attribute('value', 'Login')

    #Проверка цвета кнопки
    expected_color = hex_to_rgb_str("#3ddc91")
    expect(login.login_button).to_have_css('background-color',expected_color)

    # Функция для теста нижнего блока - форма, содержащей допустимые Username'ы и пароль
def test_futer_block (login):

    login.page.goto(project_url)

    #Проверка наличия списка допустимых Username'ов
    expect(login.cred_list).to_be_visible()
    expect(login.cred_list).to_contain_text(cred_list_text)

    #Проверка наличия допустимого пароля
    expect(login.cred_passwords).to_be_visible()
    expect(login.cred_passwords).to_contain_text('Password for all users:secret_sauce')

def test_auth_happy_path (login):

    #username_list = ('standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user')
    #password = secret_sauce

    login.page.goto(project_url)

    #Проверка окружения - поля ввода и кнопка Login на месте
    expect(login.username_field).to_be_visible()
    expect(login.password_field).to_be_visible()
    expect(login.login_button).to_be_visible()

    #Действия
    login.username_field.fill('standard_user') # заполнить поле username текстом standard_user
    login.password_field.fill('secret_sauce')

    # Сделать скрин с заполненным полем
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    login.page.screenshot(path=f"screenshots/username_filled_{timestamp}.png")

    login.login_button.click() #нажать кнопку Login

    #Проверки после клика

    expect(login.page).to_have_url(project_url_after_auth)

def test_auth_blank_fields_error(login):

    login.page.goto(project_url)

    # Проверка окружения - поля ввода и кнопка Login на месте
    expect(login.auth_block).to_be_visible()
    expect(login.login_button).to_be_visible()

    login.login_button.click()

    #Проверки после клика
    expect(login.error_box).to_contain_text('Epic sadface: Username is required')  # ворнинг содержит нужный тест ошибки
    expected_color = hex_to_rgb_str("#e2231a")  # конвертация hex → rgb
    expect(login.error_box).to_have_css('background-color', expected_color)  # ворнинг нужного цвета
    expect(login.error_button).to_be_visible() #ворнинг содержит крестик для закрытия


    for i in range(login.error_warning_pics.count()):
        expect(login.error_warning_pics.nth(i)).to_be_visible() #отображаются крестики в полях ввода


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    login.page.screenshot(path=f"screenshots/after_login_click_{timestamp}.png")

    login.error_button.click()

    #Проверки после клика
    expect(login.error_box).to_contain_text('')  # ворнинг пустой
    expect(login.error_box).to_have_css('background-color', 'rgb(255, 255, 255)')
    expect(login.error_button).to_be_hidden()

    for i in range(login.error_warning_pics.count()):
        expect(login.error_warning_pics.nth(i)).to_be_hidden()


def test_auth_one_field_blank_error (login):

    #username_list = ('standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user')

    login.page.goto(project_url)

    #Проверка окружения - поля ввода и кнопка Login на месте
    expect(login.username_field).to_be_visible()
    expect(login.password_field).to_be_visible()
    expect(login.login_button).to_be_visible()

    #Действия
    login.username_field.fill('standard_user') # заполнить поле username текстом standard_user

    # Сделать скрин с заполненным полем
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    login.page.screenshot(path=f"screenshots/username_filled_{timestamp}.png")

    login.login_button.click() #нажать кнопку Login

    #Проверки после клика
    expect(login.error_box).to_contain_text('Epic sadface: Password is required')  # ворнинг содержит нужный тест ошибки
    expected_color = hex_to_rgb_str("#e2231a")  # конвертация hex → rgb
    expect(login.error_box).to_have_css('background-color', expected_color)  # ворнинг нужного цвета
    expect(login.error_button).to_be_visible() #ворнинг содержит крестик для закрытия
    for i in range(login.error_warning_pics.count()):
        expect(login.error_warning_pics.nth(i)).to_be_visible() #отображаются крестики в полях ввода

    #Сделать скрин с текстом ошибки
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    login.page.screenshot(path=f"screenshots/after_empty_password_click_{timestamp}.png")

    #Закрыть ошибку
    login.error_button.click()

#def test_auth_invalid_fill_error





