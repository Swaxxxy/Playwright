import webcolors
project_url = 'https://www.saucedemo.com'
project_url_after_auth = 'https://www.saucedemo.com/inventory.html'
cred_list_text = """Accepted usernames are:standard_userlocked_out_userproblem_userperformance_glitch_usererror_uservisual_user"""


def hex_to_rgb_str(hex_color):
    rgb = webcolors.hex_to_rgb(hex_color)
    return f"rgb({rgb.red}, {rgb.green}, {rgb.blue})"
