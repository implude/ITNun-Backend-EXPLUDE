import pandas as pd
import datetime, requests, urllib.parse
from bs4 import BeautifulSoup

def crawl_news_list() -> tuple:
    df: pd.DataFrame = pd.read_html('https://www.youthcenter.go.kr/board/boardList.do?bbsNo=3&pageUrl=board/board', encoding='utf-8', header=0)[0] 

    for i in range(len(df)):
        val: str = df.at[i,'번호'].replace("번호", "").replace(" ", "")
        if val == '공지':
            continue
        starting_index: int = i
        break
    for i in range(starting_index, len(df)):
        uploaded_date: datetime.datetime = datetime.datetime.strptime(df.at[i, '등록일'].replace("등록일", "").replace(" ", ""), "%Y.%m.%d")
        if uploaded_date < datetime.datetime.now() - datetime.timedelta(days=7):
            ending_index: int = i
            break
    
    if ending_index > starting_index:
        return int(df.at[starting_index,'번호'].replace("번호", "").replace(" ", "")), int(df.at[ending_index,'번호'].replace("번호", "").replace(" ", ""))
    else:
        return 0, 0

def crawl_news_contents() -> list:
    news_dict_list: list = []
    url: str = 'https://www.youthdaily.co.kr/news/section_list_all.html?sec_no=54&page=1'
    params: dict = {'sec_no': 54, 'page': 1}
    response: requests.Response = requests.get(url, params=params)
    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
    for i in range(1,4):
        li_object = BeautifulSoup(str(soup.select('#container > div > div:nth-child(1) > div > div.ara_001 > ul > li:nth-child({0})'.format(i))), 'html.parser').find('a')
        
        news_dict_list.append({'title': li_object.find("h2").text, 'date': li_object.find("ul").find_all("li")[1].text, 'content': li_object.find('p').text, 'url': "https://www.youthdaily.co.kr" + li_object.get_attribute_list("href")[0]})
    return news_dict_list

def crawl_news() -> list:
    return crawl_news_contents(crawl_news_list())

print(crawl_news_contents())