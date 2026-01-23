# Селекторы основной страницы
from requests import options

#page_selectors
menu_button = '#react-burger-menu-btn'
filter_button = '[data-test="product-sort-container"]'
cart = '[data-test="shopping-cart-link"]'
cart_badge = '[data-test="shopping-cart-badge"]'

#card_selectors
card_header = '[data-test="inventory-item-name"]'
card_description = '[data-test="inventory-item-desc"]'
card_price = '[data-test="inventory-item-price"]'
card_img = '[data-test="inventory-item-sauce-labs-bike-light-img"]'

# это селектор для кнопки внутри КОНКРЕТНОЙ карточки
card_add_button = '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]'
card_remove_button = '[data-test="remove-sauce-labs-bolt-t-shirt"]'

#checkout
checkout_button = '[data-test="checkout"]'
checkout_button_continue = '[data-test="continue"]'

#checkout_info
checkout_info_first_name = '[data-test="firstName"]'
checkout_info_last_name = '[data-test="lastName"]'
checkout_info_zip_code = '[data-test="postalCode"]'
checkout_button_finish = '[data-test="finish"]'

logo = '[data-test="pony-express"]'