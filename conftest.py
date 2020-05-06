import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Choose the browser: 'chrome' or 'firefox'")
    parser.addoption("--language", action="store", default="en",
                     help="Choose browser language for use in this test, e.g 'en', 'de', 'fr', etc.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        opts = Options()
        opts.add_experimental_option("prefs", {"intl.accept_languages": language})
        print("\nStart Chrome browser for test...")
        browser = webdriver.Chrome(options=opts)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        print("\nStart Firefox browser for test...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser should be 'chrome' or 'firefox'")
    yield browser
    print("\nQuit browser...")
    browser.quit()
