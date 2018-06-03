# -*- coding: utf-8 -*-
import codecs
import pymysql


def dump(a, b):
    print(str(a) + " \"" + str(b) + "\"")


def add(aid, articleTitle, articleDate, articleTxt):
    #   conn = pymysql.connect(host='192.168.0.1', user='root',
    #   password='high1uck', db='info', charset='utf8')

    #   curs = conn.cursor()
    #   sql = """insert into customer(aid,articleTitle,articleDate,sex,major,
    #   year,name,bus,subway,place) values (%s, %s, %s, %s, %s,
    #   %s, %s, %s, %s, %s)"""
    tList = ["sex", "major", "year", "name", "bus", "subway", "place"]
    l = (aid, articleTitle, articleDate)
    for target in tList:
        f = codecs.open(target + ".txt", 'r')
        lines = f.readlines()
        element = None
        for line in lines:
            frags = line.split(":")
            cnt = 0
            mainFrag = frags[0]
            for i in frags:
                if i is '\n': continue
                if articleTitle.find(i) is not -1:
                    cnt = 1
                elif articleTxt.find(i) is not -1:
                    cnt = 1
            if cnt is not 0:
                element = mainFrag
                break
        l += (element,)
    print(l)

if __name__ == "__main__":
    add("2211659.", "오늘 열시반 미학 발표하신 분", "0001.01.01 00:00", "인"
        "상주의 발표하신 정외과 남자분 !\n 목소리 너무 좋으셨어요ㅠㅠ"
        "asmr 해주셨으면 하는 목소리...\n 다시 목소리 들을 일은 없겠지"
        "만 ㅠ 발표하시는동안 경청했습니다 ㅎㅎㅎ 발표 수고하셨어요 !")
