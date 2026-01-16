import webcolors
import os
from datetime import datetime
project_url = 'https://www.saucedemo.com'
project_url_after_auth = 'https://www.saucedemo.com/inventory.html'
cred_list_text = """Accepted usernames are:standard_userlocked_out_userproblem_userperformance_glitch_usererror_uservisual_user"""
valid_username = 'standard_user'
valid_password = 'secret_sauce'
filter_name_text_asc = 'Name (A to Z)'
filter_name_text_desc='Name (Z to A)'
filter_name_price_asc= 'Price (low to high)'
filter_name_price_desc= 'Price (high to low)'

def hex_to_rgb_str(hex_color):
    rgb = webcolors.hex_to_rgb(hex_color)
    return f"rgb({rgb.red}, {rgb.green}, {rgb.blue})"

def take_screenshot(page,name):
    test_name = name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    screenshots_path = os.path.join(project_root, "screenshots")
    page.screenshot(path=os.path.join(screenshots_path, f"{test_name}_{timestamp}.png"))