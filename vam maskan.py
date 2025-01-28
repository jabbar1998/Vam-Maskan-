import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException, \
    ElementClickInterceptedException, StaleElementReferenceException


class Vam:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://saman.mrud.ir/")

    def wait_for_element(self, by, value, timeout=180):
        while True:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((by, value))
                )
                return element
            except (TimeoutException, NoSuchElementException, StaleElementReferenceException):
                print(f"Retrying to find element {value}")
                continue

    def click_element(self, by, value, timeout=180):
        while True:
            try:
                element = self.wait_for_element(by, value, timeout)
                element.click()
                return
            except (
                    ElementClickInterceptedException, TimeoutException, NoSuchElementException,
                    StaleElementReferenceException):
                print(f"Retrying to click element {value}")
                time.sleep(1)
                continue

    def element_exists(self, by, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
            return True
        except TimeoutException:
            return False

    def find_element_by_text(self, tag_name, text, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, f"//{tag_name}[contains(text(), '{text}')]"))
            )
            return element
        except TimeoutException:
            return None
    def find_element_by_class_and_text(self, class_name, text, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
            )
            for element in elements:
                if text in element.text:
                    return element
            return None
        except TimeoutException:
            return None

    def entery_form(self):
        self.click_element(By.XPATH, '/html/body/div/div/div/main/div/div/div[2]/a[1]')
        self.click_element(By.XPATH, '/html/body/div/div/div/main/div/div/div/div[1]/div/div/a')
        username_field = self.wait_for_element(By.ID, 'username')
        username_field.send_keys("09307212580")
        time.sleep(3)
        self.click_element(By.ID, 'send-otp-form-btn')
        time.sleep(8)
        self.click_element(By.XPATH, '/html/body/div/div/div/main/div/div/div[2]/a[1]')
        self.click_element(By.XPATH, '/html/body/div/div/div/main/div/div/div/div/div[1]/div/div[2]/div/div[3]')
        time.sleep(3)
        self.click_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[1]/a/div[2]/a')
        while True:
            try:
                self.click_element(By.XPATH, '//*[@id="app"]/div/main/div/div/div/div/div[2]/a[2]')
                time.sleep(1)
                self.click_element(By.XPATH,
                                   '//*[@id="app"]/div[2]/div/div/div[2]/form/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/div')
                time.sleep(5)
                wait = WebDriverWait(self.driver, 10)
                element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'سپه')]")))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'سپه')]")))
                element.click()
                time.sleep(3)
                xpath_to_check = '//*[@id="app"]/div[2]/div/div/div[2]/form/div[3]/div/div/div/div[2]/div/div'
                if self.element_exists(By.XPATH, xpath_to_check):
                    print("Bank Close !!!!!!!!!! ")
                    self.driver.refresh()
                    time.sleep(5)
                    continue
                else:
                    print(" !!!!!!!!!!!  Bank Open  !!!!!!!!!! ")
                    time.sleep(50)
                    break
            except Exception as e:
                print(f"An error occurred: {e}")
                self.driver.refresh()
                time.sleep(5)
                continue

    def check_class_exists(self, class_name):
        try:
            elements = self.driver.find_elements(By.CSS_SELECTOR, f".{class_name.replace(' ', '.')}")
            return len(elements) > 0
        except Exception as e:
            print(f"Error checking class: {e}")
            return False


vam = Vam()
vam.entery_form()
