from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec, wait
import time

class WebScrapper():

    def __init__(self):
        self.url = "https://covid.saude.gov.br/"
        self.driver = ''
        self.wait = ''
        self.action = ''
        self.path_download = 'C:\\temp1'
        self.btn_download = '/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[6]/div[1]'

    def start_Driver(self):
        chromeOptions = webdriver.ChromeOptions()
        prefs = {"download.default_directory": self.path_download,
                 "directory_upgrade": True}

        chromeOptions.add_experimental_option("prefs", prefs)

        chromeOptions.add_argument("--incognito")
        self.driver = webdriver.Chrome(chrome_options=chromeOptions, executable_path='chromedriver.exe')
        self.wait = WebDriverWait(self.driver, 60)

        # URL principal
        self.driver.get(self.url)

        self.action = ActionChains(self.driver);

        #self.driver.execute_script('window.scrollBy(200, 0)')

    def download_csv(self):
        time.sleep(6)

        body = self.driver.find_element_by_xpath('/html/body')
        body.click()
        for i in range(0,20):
            ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()

        time.sleep(2)

        csv_btn = self.wait.until(
            ec.visibility_of_element_located(
                (By.XPATH, self.btn_download)))
        csv_btn.click()
        time.sleep(10)
        print('Arquivo baixado!')

def main():

    webscrapper = WebScrapper()
    webscrapper.start_Driver()
    webscrapper.download_csv()
    webscrapper.driver.close()

if __name__ == '__main__':
    main()

