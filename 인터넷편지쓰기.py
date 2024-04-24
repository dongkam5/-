from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import os
import time

Name="이름"
Year="연"
Month="월"
Day="일"
title="제목"
content="내용"
password="비밀번호!"


# *********************************************************************************************************************************************#











driver = webdriver.Chrome(ChromeDriverManager().install())
browser =driver
# options = webdriver.ChromeOptions()
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# browser = webdriver.Chrome(options=options)
browser.maximize_window() # 창 최대화

url = "https://www.airforce.mil.kr/user/indexSub.action?codyMenuSeq=156893223&siteId=last2&menuUIType=top"
browser.get(url)
# url = "https://www.google.com/"
# browser.get(url)

# input_=browser.find_element(By.CLASS_NAME,'gLFyf') # 구글 입력창
# input_.send_keys("공군기본군사훈련단 편지쓰기") #검색어 입력
# input_.send_keys(Keys.ENTER) # 엔터 입력
# search_=browser.find_element(By.CLASS_NAME,"yuRUbf") # 인터넷 편지를 감싸는 div 
# search_.find_element(By.TAG_NAME,"a").click() # div 안의 a 링크 클릭
try:
    tbody=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.TAG_NAME,'tbody'))) # 입력을 받는 tbody 
except:
    browser.quit()
input_=tbody.find_elements(By.TAG_NAME,"input") # tbody 내의 입력창 들을 받음
input_[0].send_keys(Name) #이름
input_[1].send_keys(Year) # 생년
input_[2].send_keys(Month) # 생월
input_[3].send_keys(Day) # 생일
btn=browser.find_element(By.CLASS_NAME,"UIbtn").find_element(By.ID,"btnNext") # 입력 후 다음 창으로 가는 버튼
btn.click() # 클릭

browser.switch_to.window(browser.window_handles[1]) # 새로운 창으로 변환
browser.find_element(By.CLASS_NAME,"choice").click() # 교육생 맞다고 확인 버튼 클릭
browser.switch_to.window(browser.window_handles[0]) # 메인 창으로 다시 변환
btn=browser.find_element(By.CLASS_NAME,"UIbtn").find_element(By.ID,"btnNext") # 다시 다음 창으로 가는 버튼 클릭
btn.click()
try:
    uibtn=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,'UIbtn'))) #인터넷 편지쓰기 버튼을 감싸는 span
except:
    browser.quit()
uibtn.find_element(By.TAG_NAME,"input").click() #span 속 button을 클릭

try:
    View=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,"UIview")))
except:
    browser.quit()
View.find_element(By.TAG_NAME,"input").click()
browser.switch_to.window(browser.window_handles[1]) # 새로운 창으로 변환
# browser.find_element(By.ID,"proceed-button").click()
input_=browser.find_element(By.CLASS_NAME,"popSearchInput")
input_.send_keys("아주대")
input_.send_keys(Keys.ENTER)
browser.find_element(By.ID,"roadAddrDiv3").click()
addrDetail=browser.find_element(By.ID,"rtAddrDetail")
addrDetail.send_keys("남제관")
browser.find_element(By.CLASS_NAME,"btn-bl").click()
browser.switch_to.window(browser.window_handles[0])
browser.find_element(By.ID,"senderName").send_keys("{}친구".format(Name)) #작성자
browser.find_element(By.ID,"relationship").send_keys("{}친구".format(Name)) #관계
browser.find_element(By.XPATH,'//*[@id="title"]').send_keys(title) #제목
browser.find_element(By.TAG_NAME,"textarea").send_keys(content) #내용
browser.find_element(By.ID,"password").send_keys(password) #비밀번호
uibtn=browser.find_element(By.CLASS_NAME,"UIbtn")
uibtn.find_element(By.TAG_NAME,"input").click()
time.sleep(5)
browser.quit()