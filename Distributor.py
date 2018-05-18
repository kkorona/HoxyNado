# -*- coding: utf-8 -*-
import codecs
import pymysql


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
    add("111", "16 경영 ㄱㄴㄷ", "0001.01.01 00:00",
        "남친 있나요?")
