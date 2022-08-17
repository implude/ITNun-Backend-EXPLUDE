import pandas as pd
import datetime, requests
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

def crawl_news_contents(index_tuple: tuple):
    news_list: list = []

    for i in range(index_tuple[0], index_tuple[1], -1):
        url: str = 'https://www.youthcenter.go.kr/board/boardDetail.do'
        params: dict = {'bbsNo': 3, 'ntceStno': i + 126, 'pageUrl': 'board%2Fboard'}
        response: requests.Response = requests.get(url, params=params)
        soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
        news_list.append(soup.find('div', 'view-txt').text)

    return news_list