# 検温の自動送信bot
from selenium import webdriver
import time
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import random
import smtplib
from email.mime.text import MIMEText
import datetime

# プロファイルフォルダを指定してChromeDriverを立ち上げる
options = Options()
PROFILE_PATH = r'〇〇〇'  # プロフィールPATHを指定 # chromeでchrome://version/と検索→プロフィールパスを入力(末尾は/User Data)
options.add_argument('--user-data-dir=' + PROFILE_PATH)
chrome_service = fs.Service(executable_path="C:\\forms_bot\\chromedriver.exe")
browser = webdriver.Chrome(service=chrome_service, options=options)
# 検温のformsのURLを取得
browser.get('https://forms.office.com/Pages/ResponsePage.aspx?id=XYP-cpVeEkWK4KezivJfyFZpkCmlsENDub1gWZtOw_tUOFNOWVRCVjg3QkpKVlBYTlpNRUxCTFZORS4u')
browser.switch_to.default_content()
time.sleep(7)
# 体温入力
list = [36.4, 36.5, 36.6]
choice = random.choice(list)
print(choice)
element = browser.find_element(by=By.XPATH, value='//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div/div/input')
element.clear()
element.send_keys(choice)
browser.close()
# 一度formsを閉じる
# プロファイルフォルダを指定してChromeDriverを立ち上げる
options = Options()
PROFILE_PATH = r'C:\Users\81702\AppData\Local\Google\Chrome\User Data'  # プロフィールPATHを指定
options.add_argument('--user-data-dir=' + PROFILE_PATH)
chrome_service = fs.Service(executable_path="C:\\forms_bot\\chromedriver.exe")
browser = webdriver.Chrome(service=chrome_service, options=options)
browser.get('https://forms.office.com/Pages/ResponsePage.aspx?id=XYP-cpVeEkWK4KezivJfyFZpkCmlsENDub1gWZtOw_tUOFNOWVRCVjg3QkpKVlBYTlpNRUxCTFZORS4u')
browser.switch_to.default_content()
time.sleep(7)
# 送信
element = browser.find_element(by=By.XPATH, value='//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/div')
element.click()
time.sleep(5)

# 送信完了のemailをgmailに送信する
# SMTP認証情報
account = "gmailのアカウント(サブ垢推奨)"
password = "上のアカウントのパスワード"
# 送受信先
to_email = "送信先のメルアド(=account)"
from_email = "送信元のメルアド(本アカでおｋ)"
# MIMEの作成
dt_now = datetime.datetime.now()
subject = '検温の送信完了'
message = '検温の送信完了' + "\n" + "送信時の時刻" + str(dt_now)
msg = MIMEText(message, 'html')
msg["subject"] = subject
msg["To"] = to_email
msg["From"] = from_email
# メール送信処理
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(account, password)
server.send_message(msg)
server.quit()
print("メールの送信完了")
print("以下mailの内容")
print("--------------------------------------")
print(message)
print("--------------------------------------")

print("検温の送信+確認用メッセージの送信完了")