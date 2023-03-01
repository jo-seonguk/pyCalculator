# 크롬 브라우저를 띄우기 위해, 웹드라이버를 가져오기
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
#from html_table_parser import parser_functions
import pandas as pd

'''     실행이 안될경우 id, class 변수명 확인, td 순서 바뀌면 다시 해줘야함
        크롬 드라이버 버전, 크롬 버전 최신인지 확인, 홈페이지 주소 확인        '''

# 검색어
query = '안전점검'
now = datetime.now()
before_one_month = now - relativedelta(months=2)
before_four_month = now - relativedelta(months=4)
pixdate = before_four_month.strftime("%Y-%m-%d")
#pixdate_datetime_format = datetime.strptime(pixdate, "%Y-%m-%d")
results = []


def geoje():    #거제
    # 입찰정보 검색 페이지로 이동
    #driver.implicitly_wait(10) # seconds
    driver.get('https://www.geoje.go.kr/index.geoje?menuCd=DOM_000008902001002001')
    
    # id값이 keyword인 태그 가져오기
    keyword = driver.find_element(By.ID, 'keyword')
    # 내용을 삭제 (버릇처럼 사용할 것!)
    keyword.clear()
    # 검색어 입력후 엔터
    keyword.send_keys(query)
    keyword.send_keys(Keys.RETURN)

    time.sleep(3)
    # 검색 버튼 클릭
    search_button = driver.find_element(By.CLASS_NAME, 'btn')
    search_button.click()
    
    # 검색 결과 확인
    elem = driver.find_element(By.CLASS_NAME, 'board-list')
    div_list = elem.find_elements(By.TAG_NAME, 'tr')

    
    # 검색 결과 모두 긁어서 리스트로 저장
    for div in div_list:
        a_tags = div.find_elements(By.TAG_NAME, 'a')
        
        if a_tags:
            for a_tag in a_tags:
                td = div.find_elements(By.TAG_NAME, "td")
                str_format = td[4].text.split('.')
                datetime_string = str_format[0] + '-' + str_format[1] + '-' + str_format[2]
                datetime_format = '%Y-%m-%d'
                datetime_result = datetime.strptime(datetime_string, datetime_format)

                if datetime_result > before_one_month:
                    results.append(datetime_string)
                    results.append(td[1].text)

                    link = a_tag.get_attribute('href')
                    results.append(link)
                else:
                    pass
                

def molit(): #국토
    # 입찰정보 검색 페이지로 이동
    #driver.implicitly_wait(10) # seconds
    driver.get('http://www.molit.go.kr/brocm/USR/BORD0201/m_20580/LST.jsp')

    # id값이 keyword인 태그 가져오기
    datepicker = driver.find_element(By.ID, 'datepicker1')
    # 내용을 삭제 (버릇처럼 사용할 것!)
    datepicker.clear()
    # 검색어 입력후 엔터
    datepicker.send_keys(pixdate)
    datepicker.send_keys(Keys.RETURN)

    time.sleep(3)
    # id값이 keyword인 태그 가져오기
    keyword = driver.find_element(By.ID, 'searchBox')
    # 내용을 삭제 (버릇처럼 사용할 것!)
    keyword.clear()
    # 검색어 입력후 엔터
    keyword.send_keys(query)
    keyword.send_keys(Keys.RETURN)


    # 검색 버튼 클릭
    search_button = driver.find_element(By.CLASS_NAME, 'bd_btn02.ml5')
    search_button.click()

    # 검색 결과 확인
    elem = driver.find_element(By.CLASS_NAME, 'bbs_list')
    div_list = elem.find_elements(By.TAG_NAME, 'tr')

    
    # 검색 결과 모두 긁어서 리스트로 저장
    for div in div_list:
        a_tags = div.find_elements(By.TAG_NAME, 'a')
        #print(div.text)
        if a_tags:
            for a_tag in a_tags:
                td = div.find_elements(By.TAG_NAME, "td")
                datetime_result = datetime.strptime(td[3].text, '%Y-%m-%d')

                if datetime_result > before_one_month:
                    results.append(datetime_string)
                    results.append(td[1].text)

                    link = a_tag.get_attribute('href')
                    results.append(link)
                else:
                    pass




                

def cng(): #창녕
    # 입찰정보 검색 페이지로 이동
    #driver.implicitly_wait(10) # seconds
    driver.get('https://www.cng.go.kr/news/00000372/00000375.web')
    
    # id값이 keyword인 태그 가져오기
    keyword = driver.find_element(By.ID, 'sstring')
    # 내용을 삭제 (버릇처럼 사용할 것!)
    keyword.clear()
    # 검색어 입력후 엔터
    keyword.send_keys(query)
    keyword.send_keys(Keys.RETURN)

    time.sleep(3)
    # 검색 버튼 클릭
    search_button = driver.find_element(By.CLASS_NAME, 'button.submit.fw20')
    search_button.click()

    # 검색 결과 확인
    elem = driver.find_element(By.CLASS_NAME, 'bbs1list1')
    div_list = elem.find_elements(By.TAG_NAME, 'li')

    
    # 검색 결과 모두 긁어서 리스트로 저장
    for div in div_list:
        a_tags = div.find_elements(By.TAG_NAME, 'a')
        
        
        if a_tags:
            for a_tag in a_tags:
                link = a_tag.get_attribute('href')
                subdate = a_tag.find_element(By.CLASS_NAME, 't3')
                subtext = a_tag.find_element(By.CLASS_NAME, 't1')

                datetime_result = datetime.strptime(subdate.text, '%Y-%m-%d')

                if datetime_result > before_one_month:
                    results.append(subdate.text)
                    results.append(subtext.text)
                    results.append(link)
                else:
                    pass
                

def miryang(): #밀양
    # 입찰정보 검색 페이지로 이동
    #driver.implicitly_wait(10) # seconds
    driver.get('https://www.miryang.go.kr/web/eMinwonList.do?mnNo=20903000000')
    
    # id값이 keyword인 태그 가져오기
    keyword = driver.find_element(By.ID, 'input-srch')
    # 내용을 삭제 (버릇처럼 사용할 것!)
    keyword.clear()
    # 검색어 입력후 엔터
    keyword.send_keys(query)
    keyword.send_keys(Keys.RETURN)

    time.sleep(3)
    # 검색 버튼 클릭
    search_button = driver.find_element(By.CLASS_NAME, 'btn-srh')
    search_button.click()

    # 검색 결과 확인
    elem = driver.find_element(By.CLASS_NAME, 'board-list-wrap')
    div_list = elem.find_elements(By.TAG_NAME, 'tr')

    
    # 검색 결과 모두 긁어서 리스트로 저장
    for div in div_list:
        a_tags = div.find_elements(By.TAG_NAME, 'a')
        
        if a_tags:
            for a_tag in a_tags:
                td = div.find_elements(By.TAG_NAME, "td")
                datetime_result = datetime.strptime(td[4].text, '%Y-%m-%d')

                if datetime_result > before_one_month:
                    results.append(td[4].text)
                    results.append(td[2].text)

                    link = a_tag.get_attribute('href')
                    results.append(link)
                else:
                    pass

def gyeongnam(): #경상남도
    # 입찰정보 검색 페이지로 이동
    #driver.implicitly_wait(10) # seconds
    driver.get('https://www.gyeongnam.go.kr/index.gyeong?menuCd=DOM_000000135003009001')

    # id값이 keyword인 태그 가져오기
    datepicker = driver.find_element(By.ID, 'conIfmStdt')
    # 내용을 삭제 (버릇처럼 사용할 것!)
    datepicker.clear()
    # 검색어 입력후 엔터
    datepicker.send_keys(pixdate)
    datepicker.send_keys(Keys.RETURN)

    
    # id값이 keyword인 태그 가져오기
    keyword = driver.find_element(By.ID, 'conTitle')
    # 내용을 삭제 (버릇처럼 사용할 것!)
    keyword.clear()
    # 검색어 입력후 엔터
    keyword.send_keys(query)
    keyword.send_keys(Keys.RETURN)

    time.sleep(3)
    # 검색 버튼 클릭
    search_button = driver.find_element(By.ID, 'searchSubmit')
    search_button.click()

    # 검색 결과 확인
    elem = driver.find_element(By.CLASS_NAME, 'board')
    div_list = elem.find_elements(By.TAG_NAME, 'tr')

    
    # 검색 결과 모두 긁어서 리스트로 저장
    for div in div_list:
        a_tags = div.find_elements(By.TAG_NAME, 'a')
        
        if a_tags:
            for a_tag in a_tags:
                td = div.find_elements(By.TAG_NAME, "td")
                datetime_result = datetime.strptime(td[4].text, '%Y-%m-%d')

                if datetime_result > before_one_month:
                    results.append(td[4].text)
                    results.append(td[2].text)

                    link = a_tag.get_attribute('href')
                    results.append(link)
                else:
                    pass


def sacheon(): #사천
    # 입찰정보 검색 페이지로 이동
    #driver.implicitly_wait(10) # seconds
    driver.get('https://www.sacheon.go.kr/news/00009/00014.web')
    
    # id값이 keyword인 태그 가져오기
    keyword = driver.find_element(By.ID, 'sstring')
    # 내용을 삭제 (버릇처럼 사용할 것!)
    keyword.clear()
    # 검색어 입력후 엔터
    keyword.send_keys(query)
    keyword.send_keys(Keys.RETURN)

    time.sleep(3)
    # 검색 버튼 클릭
    search_button = driver.find_element(By.CLASS_NAME, 'ic1.bsContain')
    search_button.click()

    # 검색 결과 확인
    elem = driver.find_element(By.CLASS_NAME, 'list1f1t3i1')
    div_list = elem.find_elements(By.TAG_NAME, 'div')

    
    # 검색 결과 모두 긁어서 리스트로 저장
    for div in div_list:
        a_tags = div.find_elements(By.TAG_NAME, 'a')

        if a_tags:
            for a_tag in a_tags:
                subdate = a_tag.find_element(By.CLASS_NAME, 't3')

                datetime_result = datetime.strptime(subdate.text, '%Y-%m-%d')

                if datetime_result > before_one_month:
                    link = a_tag.get_attribute('href')
                    subtext = a_tag.find_element(By.CLASS_NAME, 't1')
                    results.append(subdate.text)
                    results.append(subtext.text)
                    results.append(link)
                else:
                    pass


def gyeongnamload(): #경남 도로관리사무소
    # 입찰정보 검색 페이지로 이동
    #driver.implicitly_wait(10) # seconds
    driver.get('https://www.gyeongnam.go.kr/street/board/list.gyeong?boardId=BBS_0000020&menuCd=DOM_000000704001000000&contentsSid=239&cpath=%2Fstreet')

    # id값이 keyword인 태그 가져오기
    keyword = driver.find_element(By.ID, 'keyword')
    # 내용을 삭제 (버릇처럼 사용할 것!)
    keyword.clear()
    # 검색어 입력후 엔터
    keyword.send_keys(query)
    keyword.send_keys(Keys.RETURN)

    time.sleep(3)
    # 검색 버튼 클릭
    search_button = driver.find_element(By.ID, 'searchSubmit')
    search_button.click()

    # 검색 결과 확인
    elem = driver.find_element(By.CLASS_NAME, 'board')
    div_list = elem.find_elements(By.TAG_NAME, 'tr')

    
    # 검색 결과 모두 긁어서 리스트로 저장
    for div in div_list:
        a_tags = div.find_elements(By.TAG_NAME, 'a')
        
        if a_tags:
            for a_tag in a_tags:
                subdate = div.find_element(By.CLASS_NAME, 'date')

                str_format = subdate.text.split('.')
                datetime_string = "20" + str_format[0] + '-' + str_format[1] + '-' + str_format[2]
                datetime_format = '%Y-%m-%d'
                datetime_result = datetime.strptime(datetime_string, datetime_format)

                if datetime_result > before_one_month:
                    link = a_tag.get_attribute('href')
                    subtext = a_tag.get_attribute('title')
                    results.append(subdate.text)
                    results.append(subtext.text)
                    results.append(link)
                else:
                    pass
        
# 크롬 드라이버로 크롬을 실행한다.  
driver = webdriver.Chrome('chromedriver')
try:
    
    geoje()
    molit()
    cng()
    miryang()
    gyeongnam()
    sacheon()
    gyeongnamload()
    
    # 검색결과 모음 리스트를 12개씩 분할하여 새로운 리스트로 저장 
    result = [results[i * 3:(i + 1) * 3] for i in range((len(results) + 3 - 1) // 3 )]
    result.sort(reverse=True)
    
    # 결과 출력
    column_list = ['게시일', '제목', '링크']
    df = pd.DataFrame(data=result[0:], columns=column_list)
    df.to_csv("C:/Users/User/Documents/test/" + 'resultList.csv', encoding='cp949')
    
    
except Exception as e:
    # 위 코드에서 에러가 발생한 경우 출력
    print(e)
finally:
    # 에러와 관계없이 실행되고, 크롬 드라이버를 종료
    driver.quit()
