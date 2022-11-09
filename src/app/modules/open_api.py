import requests, os, xmltodict, json


def get_count_of_policy():
    url = "https://www.youthcenter.go.kr/youngPlcyUnif/youngPlcyUnifList.do"
    resp = requests.get(url)
    start_index = resp.text.find("<strong>검색건수 <span>")+19
    parsed = resp.text[start_index:]
    count = ""
    for i in parsed:
        try: 
            int(i)
            count += i
        except ValueError:
            if i == ",":
                continue
            break
    return int(count)


def get_youth_policy():
    iteration, remainder = divmod(get_count_of_policy(), 100)

    list_type = []
    url = "https://www.youthcenter.go.kr/opi/empList.do"
    api_key = os.environ.get('YOUTH_API_KEY')

    for i in range(1, iteration+2):
        params = {'openApiVlak': api_key, 'pageIndex': i, 'display': 100}
        resp = requests.get(url, params=params)
        dict_type = xmltodict.parse(resp.text)
        json_type = json.dumps(dict_type)
        if i > iteration:
            list_type = list_type + json.loads(json_type)['empsInfo']['emp'][0:remainder]
            return list_type

        list_type = list_type + json.loads(json_type)['empsInfo']['emp']
    
def get_count_of_youth_space():
    url = "https://www.youthcenter.go.kr/youngSpc/youngSpcList.do"
    resp = requests.get(url)
    start_index = resp.text.find("<strong>검색건수 <span>")+19
    parsed = resp.text[start_index:]
    count = ""
    for i in parsed:
        try: 
            int(i)
            count += i
        except ValueError:
            if i == ",":
                continue
            break
    return int(count)
def get_youth_space():
    iteration, remainder = divmod(get_count_of_youth_space(), 100)

    list_type = []
    url = "https://www.youthcenter.go.kr/opi/wantedSpace.do"
    api_key = os.environ.get('YOUTH_API_KEY')

    for i in range(1, iteration+2):
        params = {'openApiVlak': api_key, 'pageIndex': i, 'display': 100, 'pageType': 1}
        resp = requests.get(url, params=params)
        text = resp.text.replace("식음료:제공]]>", "<![CDATA[식음료:제공]]>")
        dict_type = xmltodict.parse(text)
        json_type = json.dumps(dict_type)
        if i > iteration:
            pass
            # list_type = list_type + json.loads(json_type)
        return json.loads(json_type), iteration, remainder, resp.url

        # list_type = list_type + json.loads(json_type)
def detail_youth_policy(param_dict):

    url = "https://www.youthcenter.go.kr/opi/empList.do"
    api_key = os.environ.get('YOUTH_API_KEY')

    params = {'openApiVlak': api_key, 'display': 100}
    if "query" in param_dict:
        params["query"] = param_dict["query"]
    if "bizTycdSel" in param_dict:
        params["bizTycdSel"] = param_dict["bizTycdSel"]
    if "srchPolyBizSecd" in param_dict:
        params["srchPolyBizSecd"] = param_dict["srchPolyBizSecd"]
    resp = requests.get(url, params=params)
    dict_type = xmltodict.parse(resp.text)
    json_type = json.dumps(dict_type)
    try:
        list_type = json.loads(json_type)['empsInfo']['emp']
    except KeyError:
        list_type = []
    return list_type
# big_region_dict = {
#     '서울': "003002001",
#     '부산': "003002002",
#     '대구': "003002003",
#     '인천': "003002004",
#     '광주': "003002005",
#     '대전': "003002006",
#     '울산': "003002007",
#     '경기': "003002008",
#     '강원': "003002009",
#     '충북': "003002010",
#     '충남': "003002011",
#     '전북': "003002012",
#     '전남': "003002013",
#     '경북': "003002014",
#     '경남': "003002015",
#     '제주': "003002016",
#     '세종': "003002017"}

# seoul_region_dict = {
#     '종로구': "003002001001",
#     '중구': "003002001002",
#     '용산구': "003002001003",
#     '성동구': "003002001004",
#     '광진구': "003002001005",
#     '동대문구': "003002001006",
#     '중랑구': "003002001007",
#     '성북구': "003002001008",
#     '강북구': "003002001009",
#     '도봉구': "003002001010",
#     '노원구': "003002001011",
#     '은평구': "003002001012",
#     '서대문구': "003002001013",
#     '마포구': "003002001014",
#     '양천구': "003002001015",
#     '강서구': "003002001016",
#     '구로구': "003002001017",
#     '금천구': "003002001018",
#     '영등포구': "003002001019",
#     '동작구': "003002001020",
#     '관악구': "003002001021",
#     '서초구': "003002001022",
#     '강남구': "003002001023",
#     '송파구': "003002001024",
#     '강동구': "003002001025"}
# busan_region_dict = {
#     '중구': "003002002001",
#     '서구': "003002002002",
#     '동구': "003002002003",
#     '영도구': "003002002004",
#     '부산진구': "003002002005",
#     '동래구': "003002002006",
#     '남구': "003002002007",
#     '북구': "003002002008",
#     '해운대구': "003002002009",
#     '사하구': "003002002010",
#     '금정구': "003002002011",
#     '강서구': "003002002012",
#     '연제구': "003002002013",
#     '수영구': "003002002014",
#     '사상구': "003002002015",
#     '기장군': "003002002016"}

# daegu_region_dict = {
#     '중구': "003002003001",
#     '동구': "003002003002",
#     '서구': "003002003003",
#     '남구': "003002003004",
#     '북구': "003002003005",
#     '수성구': "003002003006",
#     '달서구': "003002003007",
#     '달성군': "003002003008"}

# incheon_region_dict = {
#     '중구': "003002004001",
#     '동구': "003002004002",
#     '남구': "003002004003",
#     '미추홀구': "003002004004",
#     '연수구': "003002004005",
#     '남동구': "003002004006",
#     '부평구': "003002004007",
#     '계양구': "003002004008",
#     '서구': "003002004009",
#     '강화군': "003002004010",
#     '옹진군': "003002004011"}

# gwangju_region_dict = {
#     '동구': "003002005001",
#     '서구': "003002005002",
#     '남구': "003002005003",
#     '북구': "003002005004",
#     '광산구': "003002005005"}

# daejeon_region_dict = {
#     '동구': "003002006001",
#     '중구': "003002006002",
#     '서구': "003002006003",
#     '유성구': "003002006004",
#     '대덕구': "003002006005"}

# ulsan_region_dict = {
#     '중구': "003002007001",
#     '남구': "003002007002",
#     '동구': "003002007003",
#     '북구': "003002007004",
#     '울주군': "003002007005"}

# gyeonggi_region_dict = {
#     '수원시': "003002008001",
#     '성남시': "003002008002",
#     '의정부시': "003002008003",
#     '안양시': "003002008004",
#     '부천시': "003002008005",
#     '광명시': "003002008006",
#     '평택시': "003002008007",
#     '동두천시': "003002008008",
#     '안산시': "003002008009",
#     '고양시': "003002008010",
#     '과천시': "003002008011",
#     '구리시': "003002008012",
#     '남양주시': "003002008013",
#     '오산시': "003002008014",
#     '시흥시': "003002008015",
#     '군포시': "003002008016",
#     '의왕시': "003002008017",
#     '하남시': "003002008018",
#     '용인시': "003002008019",
#     '파주시': "003002008020",
#     '이천시': "003002008021",
#     '안성시': "003002008022",
#     '김포시': "003002008023",
#     '화성시': "003002008024",
#     '광주시': "003002008025",
#     '양주시': "003002008026",
#     '포천시': "003002008027",
#     '여주시': "003002008028",
#     '양주군': "003002008029",
#     '연천군': "003002008031",
#     '가평군': "003002008033",
#     '양평군': "003002008034"}

# gangwon_region_dict = {
#     '춘천시': "003002009001",
#     '원주시': "003002009002",
#     '강릉시': "003002009003",
#     '동해시': "003002009004",
#     '태백시': "003002009005",
#     '속초시': "003002009006",
#     '삼척시': "003002009007",
#     '홍천군': "003002009008",
#     '횡성군': "003002009009",
#     '영월군': "003002009010",
#     '평창군': "003002009011",
#     '정선군': "003002009012",
#     '철원군': "003002009013",
#     '화천군': "003002009014",
#     '양구군': "003002009015",
#     '인제군': "003002009016",
#     '고성군': "003002009017",
#     '양양군': "003002009018"}

# chungbuk_region_dict = {
#     '청주시': "003002010001",
#     '충주시': "003002010002",
#     '제천시': "003002010003",
#     '청원군': "003002010004",
#     '보은군': "003002010005",
#     '옥천군': "003002010006",
#     '영동군': "003002010007",
#     '증평군': "003002010008",
#     '진천군': "003002010009",
#     '괴산군': "003002010010",
#     '음성군': "003002010011",
#     '단양군': "003002010012"}

# chungnam_region_dict = {
#     '천안시': '003002011001',
#     '공주시': '003002011002', 
#     '보령시': '003002011003', 
#     '아산시': '003002011004', 
#     '서산시': '003002011005', 
#     '논산시': '003002011006', 
#     '계룡시': '003002011007', 
#     '당진시': '003002011008', 
#     '금산군': '003002011009', 
#     '연기군': '003002011010', 
#     '부여군': '003002011011', 
#     '서천군': '003002011012', 
#     '청양군': '003002011013', 
#     '홍성군': '003002011014', 
#     '예산군': '003002011015', 
#     '태안군': '003002011016', 
#     '당진군': '003002011017'}

# jeonbuk_region_dict = {
#     '전주시': '003002012001', 
#     '군산시': '003002012002', 
#     '익산시': '003002012003', 
#     '정읍시': '003002012004', 
#     '남원시': '003002012005', 
#     '김제시': '003002012006', 
#     '완주군': '003002012007', 
#     '진안군': '003002012008', 
#     '무주군': '003002012009', 
#     '장수군': '003002012010', 
#     '임실군': '003002012011', 
#     '순창군': '003002012012', 
#     '고창군': '003002012013', 
#     '부안군': '003002012014'
# }

# jeonnam_region_dict = {
#     '목포시': '003002013001', 
#     '여수시': '003002013002', 
#     '순천시': '003002013003', 
#     '나주시': '003002013004', 
#     '광양시': '003002013005', 
#     '담양군': '003002013006', 
#     '곡성군': '003002013007', 
#     '구례군': '003002013008', 
#     '고흥군': '003002013009', 
#     '보성군': '003002013010', 
#     '화순군': '003002013011', 
#     '장흥군': '003002013012', 
#     '강진군': '003002013013', 
#     '해남군': '003002013014', 
#     '영암군': '003002013015', 
#     '무안군': '003002013016', 
#     '함평군': '003002013017', 
#     '영광군': '003002013018', 
#     '장성군': '003002013019', 
#     '완도군': '003002013020', 
#     '진도군': '003002013021', 
#     '신안군': '003002013022'
# }

# gyeongbuk_region_dict = {
#     '포항시': '003002014001', 
#     '경주시': '003002014002', 
#     '김천시': '003002014003', 
#     '안동시': '003002014004', 
#     '구미시': '003002014005', 
#     '영주시': '003002014006', 
#     '영천시': '003002014007', 
#     '상주시': '003002014008', 
#     '문경시': '003002014009', 
#     '경산시': '003002014010', 
#     '군위군': '003002014011', 
#     '의성군': '003002014012', 
#     '청송군': '003002014013', 
#     '영양군': '003002014014', 
#     '영덕군': '003002014015', 
#     '청도군': '003002014016', 
#     '고령군': '003002014017', 
#     '성주군': '003002014018', 
#     '칠곡군': '003002014019', 
#     '예천군': '003002014020', 
#     '봉화군': '003002014021', 
#     '울진군': '003002014022', 
#     '울릉군': '003002014023'}

# gyeongnam_region_dict = {
#     '창원시': '003002015001', 
#     '마산시': '003002015002', 
#     '진주시': '003002015003', 
#     '진해시': '003002015004', 
#     '통영시': '003002015005', 
#     '사천시': '003002015006', 
#     '김해시': '003002015007', 
#     '밀양시': '003002015008', 
#     '거제시': '003002015009', 
#     '양산시': '003002015010', 
#     '의령군': '003002015011', 
#     '함안군': '003002015012', 
#     '창녕군': '003002015013', 
#     '고성군': '003002015014', 
#     '남해군': '003002015015', 
#     '하동군': '003002015016', 
#     '산청군': '003002015017', 
#     '함양군': '003002015018', 
#     '거창군': '003002015019', 
#     '합천군': '003002015020'
# }

# jeju_region_dict = {
#     '제주시': '003002016001', 
#     '서귀포시': '003002016002', 
#     '북제주군': '003002016003', 
#     '남제주군': '003002016004'}

# sejong_region_dict = {
#     "세종": '003002017001'
# }