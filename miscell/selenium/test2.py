from selenium import webdriver
from selenium.webdriver.ie.service import Service

def f():
    options = webdriver.IeOptions()
    options.ignore_protected_mode_settings = True
    options.ignore_zoom_level = True
    ser = Service(
        r"..\..\..\_common\IEDriverServer_win32.exe"
    )
    driver = webdriver.Ie(
        service=ser,
        options=options
    )
    driver.get("https://yandex.ru")

f()
