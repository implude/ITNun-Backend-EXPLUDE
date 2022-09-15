# ITNun-EXPLUDE-BackEnd

## 1. Installation

1. Install docker and set docker environment variable
2. Clone thie repository
3. Prepare MariaDB or MySQL Database
4. Prepare youthcenter.go.kr OpenAPI Key
5. Make and edit .env file (the guideline file provided .env_template)
6. run with `sudo bash run.js`

## 2. API Docs

1. /check_server  GET
    
    check server
    
    ```json
    //response
    
    {
        "status": "OK"
    }
    ```
    

1. /auth/login  POST
    
    process login request
    
    ```json
    //request
    
    {
        "user_email": "seonwoo0808@pentag.kr",
        "user_pw": "yourpassword1234"
    }
    ```
    
    ```json
    //response
    
    {
        "result": "success",
        "token": "eyJ0eXAiOiJdfV1QiLCJhqqc9OiJIUzI1NrJ9.eyJ1c2VnX2VtYWysIjoic2VvbndvbzA4MdgAbmF2ZXIuY29tIiwidXNlcl9wdyI6IjRmNWfegY2Q4ODVkYTkyZjFjN2Y4NDIwNmI3ODQ0ZjU4NDI5MDU5ZGU5YWI4OTUwNmM0MjZkYzdkYTIyOTA3ZTIiLCJleHAiOjE2NjU4MzY1NTd9.dFdeChThh1y3u2nnYKTuoNULPq35rv4RtN-SiTugPgI"
    }
    
    //or 
    
    {
        "result": "fail"
    }
    ```
    

1. /auth/signin  POST
    
    process sign up request
    
    ```json
    //request
    
    {
        "user_email": "seonwoo0808@pentag.kr",
        "user_pw": "yourpassword1234!!",
        "user_job_status": "job seeker",
        "user_academic_status": "graduate",
        "user_specialization":"Engineering",
        "user_pre_startup": true
    
    }
    ```
    
    ```json
    //response
    
    {
        "result": "success"
    }
    
    //or
    
    {
        "message": "invalid params",
        "result": "fail"
    }
    
    //or 
    
    {
        "message": "user already exists",
        "result": "fail"
    }
    ```
    

1. /policy/get_all_policy  POST
    
    load all Youth Policy
    
    ```json
    //request
    {
        "token": "token earned on /auth/login"
    }
    ```
    
2. /policy/get_policy  POST
    
    load Youth Policy which user have not requested with this endpoint
    
    ```json
    //request
    {
        "token": "token earned on /auth/login"
    }
    ```
    
    ```json
    //response
    {
        "policy": [
            {
                "policy_Biz_code": "003002010",
                "policy_academic_status": "제한없음",
                "policy_age": "제한없음",
                "policy_description": "청년정책 관한 주요사항의 심의 조정을 위한 기능으로 위촉직 위원 모집",
                "policy_good_at": "제한없음",
                "policy_id": "R2022091404483",
                "policy_job_status": "제한없음",
                "policy_name": "22년 청년정책조정위원회",
                "policy_progress": "우편 및 이메일 제출",
                "policy_request_deadline": "09.08 ~ 09.18(10일간)",
                "policy_specialization": "제한없음",
                "policy_spor_amount": "6명(공개모집 인원은 응모현황에 따라 변경될 수 있음)",
                "policy_spor_description": "위원회 참석 시 예산의 범위 내에서 참석수당 지급",
                "policy_type": "정책참여",
                "policy_website_url": "-"
            },
            {
                "policy_Biz_code": "003002015",
                "policy_academic_status": "제한없음",
                "policy_age": "제한없음",
                "policy_description": "경상남도에 주택을 구입하여 살고 있는 신혼부부들을 위한 주거 지원 사업",
                "policy_good_at": "제한없음",
                "policy_id": "R2022091404463",
                "policy_job_status": "제한없음",
                "policy_name": "신혼부부 주택구입 대출이자 지원사업",
                "policy_progress": "온라인신청",
                "policy_request_deadline": "09.13. ~ 09.26 (18:00까지)",
                "policy_specialization": "제한없음",
                "policy_spor_amount": "-",
                "policy_spor_description": "올해 상반기(1~6월) 이자 납부금액 지원 (최대 75만원)",
                "policy_type": "주거·금융",
                "policy_website_url": "-"
            },
            {
                "policy_Biz_code": "003002001",
                "policy_academic_status": "-",
                "policy_age": "제한없음",
                "policy_description": "이사가 잦은 청년가구 주거비 부담 경감하기 위한 사업",
                "policy_good_at": "-",
                "policy_id": "R2022091304443",
                "policy_job_status": "-",
                "policy_name": "2022 청년 이사비 지원사업",
                "policy_progress": "청년 몽땅 정보통 온라인 신청",
                "policy_request_deadline": "09.06 ~ 09.26",
                "policy_specialization": "-",
                "policy_spor_amount": "약 5,000여명 (이사비 지원사업 예산 범위 내)",
                "policy_spor_description": "이사비 최대 40만원 한도 내 실비 지원(생애 1회 지원)",
                "policy_type": "주거·금융",
                "policy_website_url": "https://youth.seoul.go.kr/site/main/home"
            }, ......
    	]
    }
    ```
    
3. /youth_space/get_all_youth_space POST
    
    load all Youth Space
    
    ```json
    //request
    {
        "token": "token earned on /auth/login"
    }
    ```
    
    ```xml
    //response
    
    <?xml version="1.0" encoding="UTF-8"?>
    <spacesInfo>
        <totalCnt>181</totalCnt>
        <pageIndex>1</pageIndex>
        <space>
            <rownum>1</rownum>
            <spcId>201808220002</spcId>
            <spcName>
                <![CDATA[2030청년창업지원센터]]>
            </spcName>
            <areaCpvn>
                <![CDATA[대구]]>
            </areaCpvn>
            <areaSggn>
                <![CDATA[대구 중구]]>
            </areaSggn>
            <address>
                <![CDATA[대구광역시 중구 경상감영길 176]]>
            </address>
            <spcTime>
                <![CDATA[월-금 09:00-18:00]]>
            </spcTime>
            <operOrgan>
                <![CDATA[ 대구광역시청 (사)대구의료관광진흥원]]>
            </operOrgan>
            <homepage>
                <![CDATA[http://www.jung2030.or.kr]]>
            </homepage>
            <telNo>
                <![CDATA[053-424-2039]]>
            </telNo>
            <officeHours>
                <![CDATA[월-금 09:00-18:00]]>
            </officeHours>
            <openDate>
                <![CDATA[2011년 03월 01일]]>
            </openDate>
            <applyTarget>
                <![CDATA[2030청년창업프로젝트 선발자]]>
            </applyTarget>
            <spcType>
                <![CDATA[통합지원형,창업지원형]]>
            </spcType>
            <majorForm>
                <![CDATA[라운지(1개 총null명),회의실(1개 총null명),개인학습실(1개 총null명)]]>
            </majorForm>
            <spcCost>
                <![CDATA[무료]]>
            </spcCost>
            <addFacilCost>
                <![CDATA[무료]]>
            </addFacilCost>
            <foodYn>
                <![CDATA[식음료:제공안함]]>
            </foodYn>
        </space>
        <space>
            <rownum>2</rownum>
            <spcId>201902210005</spcId>
            <spcName>
                <![CDATA[JOB+공간더하기]]>
            </spcName>
            <areaCpvn>
                <![CDATA[경기]]>
            </areaCpvn>
            <areaSggn>
                <![CDATA[경기 남양주시]]>
            </areaSggn>
            <address>
                <![CDATA[경기도 남양주시 경춘로 953]]>
            </address>
            <spcTime>
                <![CDATA[월-금 10:00-18:00(주말, 공휴일 제외)]]>
            </spcTime>
            <operOrgan>
                <![CDATA[남양주시청]]>
            </operOrgan>
            <homepage>
                <![CDATA[https://blog.naver.com/nyjnavi]]>
            </homepage>
            <telNo>
                <![CDATA[031-590-2680]]>
            </telNo>
            <officeHours>
                <![CDATA[월-금 10:00-18:00(주말, 공휴일 제외)]]>
            </officeHours>
            <openDate>
                <![CDATA[2017년 06월 28일]]>
            </openDate>
            <applyTarget>
                <![CDATA[만18-만39세 청년, 구인구직매칭데이 참여자 등]]>
            </applyTarget>
            <spcType>
                <![CDATA[취업지원형]]>
            </spcType>
            <majorForm>
                <![CDATA[라운지(1개 총null명)]]>
            </majorForm>
            <spcCost>
                <![CDATA[무료]]>
            </spcCost>
            <addFacilCost>
                <![CDATA[무료]]>
            </addFacilCost><foodYn><![CDATA[식음료:제공]]></foodYn>
    </space>
    ```
