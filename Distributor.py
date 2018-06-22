# -*- coding: utf-8 -*-
import codecs
import pymysql


def add(aid, articleTitle, articleDate, articleTxt): # 크롤링한 데이터 입력
    conn = pymysql.connect(host='localhost', user='root',
    password='high1uck', db='user_info', charset='utf8') # DB에 저장하기 위하여 서버에 접속할 때 사용 할 일종의 매크로

    sql = """insert into maintbl(aid,articleTitle,articleDate,sex,name,year,major,subway,place,class) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    # maintbl에 각각의 컬럼에 문자열로 입력한다.
    tList = ["sex", "major", "year", "name", "subway", "place", "class"] # 분류조건 리스트
    l = (aid, articleTitle, articleDate) # 분류된 내용들이 저장될 튜플을 생성한다. 현 3개 이외에 내용들은 반복문을 통해 추가될 예정이다.

    for target in tList: # tList에 있는 분류조건 하나씩 실행
        f = codecs.open(target + ".txt", 'r', 'utf-8') # 저장된 분류조건의 파일 읽어오기 
        lines = f.readlines() # 저장된 분류조건의 내용들 
        element = None # 분류될 요소들 초기값을 NULL값으로 한다
        for line in lines: #저장된 분류조건 내용에서 한줄씩 하기
            frags = line.split(":") # 한 줄에서 ':' 로 각각의 상세조건 구분
            cnt = 0 # 조건에 부합하는 횟수를 위한 변수
            mainFrag = frags[0] # 메인은 해당 줄의 맨 처음에 나오는 상세조건
            for i in frags:
                if i is '\n': continue # 다음 줄이 있으면 계속 반복함
                if articleTitle.find(i) is not -1: # 제목에서 상세 조건 찾아서 조건과 부합 되면 cnt 1로 변경
                    cnt = 1
                elif articleTxt.find(i) is not -1: # 내용에서 상세 조건 찾아서 조건과 부합 되면 cnt 1로 변경
                    cnt = 1
            if cnt is not 0: # 조건이 부합 할 시 해당 조건의 메인이 element가 되며 반복문을 빠져나온다.
                element = mainFrag
                break
        if element is None and target is "sex": # 성별이 NONE 일 시 NULL 값이 아닌 X를 요소에 저장한다.
            element = 'X'
        l += (element,) # 분류된 요소들을 DB에 넣기 위한 임시 튜플에 저장한다 

    try:
        with conn.cursor() as cursor: # 앞에서 만든 conn을 사용하여 미리 지정한 서버와 연결한다
            cursor.execute(sql, l)
            # maintbl에 각각의 컬럼에 문자열로 입력한다. 해당 컬럼에 채워질 데이터는 튜플 l에 임시로 저장한 요소들을 가져온다
            conn.commit()
            # 변경사항을 최종적으로 DB에 적용한다.
            

    finally: 
        conn.close() # 서버와의 접속을 종료한다.

if __name__ == "__main__":
    add("2211659", "오늘 열시반 미학 발표하신 분", "0001.01.01 00:00", "인"
        "상주의 발표하신 정외과 남자분 !\n 목소리 너무 좋으셨어요ㅠㅠ"
        "asmr 해주셨으면 하는 목소리...\n 다시 목소리 들을 일은 없겠지"
        "만 ㅠ 발표하시는동안 경청했습니다 ㅎㅎㅎ 발표 수고하셨어요 !")  # 해당 파일 단독 사용시 크롤링이 안됬기 때문에 임의로 크롤링처럼 값을 입력한다.
