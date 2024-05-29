from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import argparse

parser = argparse.ArgumentParser(description='Form')

parser.add_argument('--formType', '-t', default='school')
parser.add_argument('--auto', '-a', default='auto')
args = parser.parse_args()

chrome_options = Options()
driver = webdriver.Chrome(service=Service("D:\\chromedriver-win64\\chromedriver.exe"))

def auto(formType, auto):
    selection = formType

    if selection == 'school':
        link = 'https://jinshuju.net/f/O7JpNp'
        addItem = ''
    else:
        link = 'https://jinshuju.net/f/Sz8gxc'
        addItem = ''

    driver.get(link)

    time.sleep(0.5)
    # 时间选择

    # 学院
    academy_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[2]/div/div/div[2]/div[1]/div/div/div/span/input')
    academy_input.send_keys('信息工程学院')

    # 班级
    class_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[4]/div/div/div[2]/div[1]/div/div/div/span/input')
    class_input.send_keys('计算机202205')

    # 学号
    id_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[6]/div/div/div[2]/div[1]/div/div/div/span/input')
    id_input.send_keys('202203792')

    # 姓名
    name_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[8]/div/div/div[2]/div[1]/div/div/div/span/input')
    name_input.send_keys('邱宗森')  # 将XXX换为对应内容
    
    # QQ
    qq_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[10]/div/div/div[2]/div[1]/div/div/div/span/input')
    qq_input.send_keys('427749375')  # 将XXX换为对应内容
    
    # 手机
    phone_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[3]/div/div[12]/div/div/div[2]/div[1]/div/div/div/div/span/input')
    phone_input.send_keys('18990775070')  # 将XXX换为对应内容
    
     # Auto Submit
    if auto == 'auto':
        # Submit form
        submit_form = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[5]/div/button')
        submit_form.click()
        time.sleep(1)
        driver.quit()
        
if __name__ == '__main__':
    try:
        auto(args.formType, args.auto)
    except Exception as e:
        print(e)

print(args.auto)