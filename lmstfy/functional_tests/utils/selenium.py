from selenium import webdriver


def get_selenium_driver():
    """Retuns selenium webdriver instance.

    Selenium Firefox webdriver may fail on no display devices.
    If it fails to start Firefox driver, start PhantomJS driver instead.

    Before starting tests on CI, make sure PhantoJS is pre-installed.
    Travis CI ( which this project use ) provides pre-installed phantomjs.

    for more information,
        - [GUI and Headless Browser Testing](http://docs.travis-ci.com/user/gui-and-headless-browsers/)
    """

    try:
        driver = webdriver.Firefox()
    except:
        driver = webdriver.PhantomJS()

    return driver
