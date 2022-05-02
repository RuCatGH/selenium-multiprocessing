from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from multiprocessing import Pool
# from fake_useragent import UserAgent
# ua = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# отключение вебдрайвера от логирования
options.add_argument('--disable-blink-features=AutomationControlled')
# оключение появления всплывающего окна
# options.headless = True


url = 'https://www.youtube.com'
def open_url(url):
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url=url)
        
        time.sleep(5)
    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    urls = [url] * 4
    p = Pool(processes = 4)
    p.map(open_url, urls)