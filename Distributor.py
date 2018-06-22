# -*- coding: utf-8 -*-
import codecs
import pymysql


def dump(a, b):
    print(str(a) + " \"" + str(b) + "\"")


def add(aid, articleTitle, articleDate, articleTxt): # 크롤링한 데이터 입력
    conn = pymysql.connect(host='localhost', user='root',
    password='high1uck', db='user_info', charset='utf8') # DB에 저장하기 위하여 서버에 접속함

    sql = """insert into maintbl(aid,articleTitle,articleDate,sex,name,year,major,subway,place,class) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    tList = ["sex", "major", "year", "name", "subway", "place", "class"] # 분류조건
    l = (aid, articleTitle, articleDate)

    for target in tList: # tList에 있는 분류조건 하나씩 실행
        f = codecs.open(target + ".txt", 'r', 'utf-8') # 저장된 분류조건의 파일 읽어오기 
        lines = f.readlines() # 저장된 분류조건의 내용들 
        element = None 
        for line in lines: #저장된 분류조건 내용에서 한줄씩 하기
            frags = line.split(":") # 한 줄에서 ':' 로 각각의 상세조건 구분
            cnt = 0 # 조건에 부합하는 횟수를 위한 변수
            mainFrag = frags[0] # 메인은 처음에 나오는 상세조건
            for i in frags:
                if i is '\n': continue # 다음 줄이 있으면 계속 반복함
                if articleTitle.find(i) is not -1:
                    cnt = 1
                elif articleTxt.find(i) is not -1:
                    cnt = 1
            if cnt is not 0: # 조건이 부합 할 시 해당 조건의 내용은 메인이 되며 반복문을 빠져나온다.
                element = mainFrag
                break
        if element is None and target is "sex": # 성별이 NONE 일 시 NULL 값이 아닌 X 
            element = 'X'
        l += (element,)

    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, l)
            conn.commit()


    finally:
        print(l)
        conn.close()

if __name__ == "__main__":
    add("2211659", "오늘 열시반 미학 발표하신 분", "0001.01.01 00:00", "인"
        "상주의 발표하신 정외과 남자분 !\n 목소리 너무 좋으셨어요ㅠㅠ"
        "asmr 해주셨으면 하는 목소리...\n 다시 목소리 들을 일은 없겠지"
        "만 ㅠ 발표하시는동안 경청했습니다 ㅎㅎㅎ 발표 수고하셨어요 !")
