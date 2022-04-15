import time

def test_find_add_to_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
    'Кнопка добавления товара в корзину отсутствует'