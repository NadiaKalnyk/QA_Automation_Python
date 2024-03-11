from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class RozetkaParser:
    def __init__(self):
        self.driver = webdriver.Chrome(
            "C:/Users/admin/PycharmProjects/python_course/QA_Automation_Python/home_work_17_selenium/chromedriver")

    def parse_page(self, url, filename):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.goods-tile")))
        self.extract_and_write_to_file(filename)
        self.navigate_to_next_page()
        self.extract_and_write_to_file(filename)

    def extract_and_write_to_file(self, filename):
        ads = self.driver.find_elements(By.CSS_SELECTOR, "div.goods-tile")
        with open(filename, 'a', encoding='utf-8') as file:
            for ad in ads:
                title = ad.find_element(By.CSS_SELECTOR, "span.goods-tile__title").text.strip()
                price = ad.find_element(By.CSS_SELECTOR, "span.goods-tile__price-value").text.strip()
                file.write(f"Назва: {title}, Ціна: {price}\n")

    def navigate_to_next_page(self):
        self.driver.execute_script("window.scrollBy(0, 2000);")
        next_page_button = self.driver.find_element(By.CSS_SELECTOR,
                                                    "a.pagination__link.ng-star-inserted.pagination__link--active")
        next_page_button.click()

    def close(self):
        self.driver.quit()


parser = RozetkaParser()
parser.parse_page('https://rozetka.com.ua/ua/mobile-phones/c80003/', 'rozetka_ads.txt')
parser.close()
