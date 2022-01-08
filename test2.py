# 検温の自動送信bot
from selenium import webdriver
import time
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random

# プロファイルフォルダを指定してChromeDriverを立ち上げる
options = Options()
PROFILE_PATH = r'C:\Users\81702\AppData\Local\Google\Chrome\User Data'  # プロフィールPATHを指定
options.add_argument('--user-data-dir=' + PROFILE_PATH)
chrome_service = fs.Service(executable_path="C:\\forms_bot\\chromedriver.exe")
browser = webdriver.Chrome(service=chrome_service, options=options)
browser.get('https://forms.office.com/Pages/ResponsePage.aspx?id=XYP-cpVeEkWK4KezivJfyFZpkCmlsENDub1gWZtOw_tUOFNOWVRCVjg3QkpKVlBYTlpNRUxCTFZORS4u')
browser.switch_to.default_content()
time.sleep(3)
# 体温入力
list = [36.4, 36.5, 36.6]
choice = random.choice(list)
print(choice)
element = browser.find_element(by=By.XPATH, value='//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/input')
element.clear()
element.send_keys(choice)
browser.close()

# プロファイルフォルダを指定してChromeDriverを立ち上げる
options = Options()
PROFILE_PATH = r'C:\Users\81702\AppData\Local\Google\Chrome\User Data'  # プロフィールPATHを指定
options.add_argument('--user-data-dir=' + PROFILE_PATH)
chrome_service = fs.Service(executable_path="C:\\forms_bot\\chromedriver.exe")
browser = webdriver.Chrome(service=chrome_service, options=options)
browser.get('https://forms.office.com/Pages/ResponsePage.aspx?id=XYP-cpVeEkWK4KezivJfyFZpkCmlsENDub1gWZtOw_tUOFNOWVRCVjg3QkpKVlBYTlpNRUxCTFZORS4u')
browser.switch_to.default_content()
time.sleep(3)
# 送信
element = browser.find_element(by=By.XPATH, value='//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div')
element.click()
time.sleep(2)

print("finished")