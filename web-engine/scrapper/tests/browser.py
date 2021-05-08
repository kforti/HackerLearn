from scrapper.browser import *



def test_chrome_scrapper_driver():
    with ChromeScrapperDriver() as driver:
        assert isinstance(driver, ChromeScrapperDriver)


def test_extract():
    with ChromeScrapperDriver() as driver:
        data = driver.extract_data_from_url("https://ocw.mit.edu/index.htm")
    for d in data:
        print(d)

def test_screen_shot():
    with ChromeScrapperDriver() as driver:
        data = driver.extract_data_from_url("https://ocw.mit.edu/index.htm")
        image = driver.snap_shot()
        print(image)