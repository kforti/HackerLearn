import time
import random
from pathlib import Path

from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver

class ChromeScrapperDriver:
    def __init__(self, chrome_path=None, max_retries=3):
        self.max_retries = max_retries
        self.chrome_path = chrome_path
        if self.chrome_path is None:
            self.chrome_path = str(Path(__file__).parent.parent / 'data/chromedriver')
        self.chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("window-size=1280,800")
        self.chrome_options.add_argument("user-data-dir=selenium")
        self.chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183")
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) #options.add_argument('--disable-blink-features=AutomationControlled')

    def start(self):
        self.driver = webdriver.Chrome(executable_path=self.chrome_path, options=self.chrome_options)
        self.driver.set_page_load_timeout(10)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        return None

    def extract_data_from_url(self, url, actions=None):
        retries = 0
        requests_data = []
        while not requests_data or retries < self.max_retries:
            try:
                self.driver.get(url)
                if actions is not None:
                    self.apply_actions(actions)
            except:
                retries += 1
                continue
            time.sleep(random.randint(4, 7))
            requests_data = self.get_requests()
            retries += 1
        self.delete_requests()
        return requests_data

    def delete_requests(self):
        del self.driver.requests

    def get_requests(self):
        requests_data = []
        for request in self.driver.requests:
            if request.response:
                data = {
                    "id": request.id,
                    "method": request.method,
                    "params": request.params,
                    "path": request.path,
                    "querystring": request.querystring,
                    "url": request.url,
                    "status_code": request.response.status_code,
                    "headers": request.response.headers,
                    "body": request.body,
                    "response": {
                        "body": request.response.body.decode('utf-8', 'ignore'),
                        "headers": request.response.headers,
                        "reason": request.response.reason,
                        "status_code": request.response.status_code
                    }
                }
                requests_data.append(data)
        return requests_data

    def apply_actions(self, actions):
        for action in actions:
            action.apply(self.driver)

    def snap_shot(self):
        image = self.driver.get_screenshot_as_png()
        return image