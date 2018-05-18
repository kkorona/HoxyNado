# -*- coding: utf-8 -*-
import codecs


def add(aid, articleTitle, articleDate, articleTxt):
    tList = ["sex", "major", "year", "name", "bus", "subway", "place", "class"]
    l = []
    for target in tList:
        f = codecs.open(target + ".txt", 'r')
        lines = f.readlines()
        appended = 0
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
                l.append([target, mainFrag])
                appended = 1
        if not appended and target == "sex":
            l.append([target, "X"])
    print(l)

if __name__ == "__main__":
    add("111", "16 경영 ㄱㄴㄷ", "0001.01.01 00:00",
        "남친 있나요?")
