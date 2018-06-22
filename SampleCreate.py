# -*- coding: utf-8 -*-
import random
import codecs
import json
import pathlib

def data_to_json(data) :
    if type(data) is str : # 타占쏙옙占쏙옙 占쏙옙占쌘울옙占싱띰옙占?
        return '"' + data + '"' # 占쏙옙占쌘울옙占쏙옙 "占쏙옙 占쏙옙占쏙옙占쌍곤옙
    elif type(data) is list : # 타占쏙옙占쏙옙 占쏙옙占쏙옙트占쏙옙占?
        return list_to_json(data, data_to_json) # 占쌉쇽옙 호占쏙옙
    elif type(data) is int or type(data) is float : # 타占쏙옙占쏙옙 占쏙옙占쌘띰옙占?
        return data.__str__() # 占쌓댐옙占? 占쏙옙환
    elif type(data) is dict : # 타占쏙옙占쏙옙 dict占쏙옙占?
        return dict_to_json(data, data_to_json) # 占쌉쇽옙 호占쏙옙
    else :
        print("type占쏙옙 {}".format(type(data)))
        return '""'

def list_to_json(list, func):
    out_str = "[" # [(占쏙옙占싫?)占쏙옙 占쏙옙占쏙옙
    for val in list:
        out_str += func(val)
        out_str += ", " # ,(占쏙옙표)占쏙옙 占쏙옙占쏙옙占싶몌옙 占쏙옙占쏙옙

    if len(out_str) > 2:
        out_str = out_str[:-2]

    out_str += "]" # ](占쏙옙占싫?)占쏙옙 占쌥는댐옙
    return out_str

def dict_to_json(dict, func) :
    out_str = "{" # {(占쌩곤옙호)占쏙옙 占쏙옙占쏙옙
    for key in dict.keys() :
        out_str += ('"' + key.__str__() + '"') # 키 占쏙옙占쏙옙 "(큰 占쏙옙占쏙옙표)占쏙옙 占쏙옙占쏙옙占?
        out_str += ": " # :(占쌥뤄옙)占쏙옙占쏙옙 Key占쏙옙 Value占쏙옙 占싻몌옙
        out_str += func(dict[key])
        out_str += ", " # ,(占쏙옙표)占쏙옙 占쌍곤옙 占쏙옙占쏙옙 占싻몌옙
    if len(out_str) > 2:
        out_str = out_str[:-2]

    out_str += "}" # }(占쌩곤옙호)占쏙옙 占쌥는댐옙
    return out_str

def main():
    tList = ["sex", "major", "year", "subway", "place", "class"]
    sampleElement = "ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅍㅎ"
    n = len(sampleElement)-1
    sampleList = []

    for kk in range(0,1):
        sampleName = "" 
        for i in range(0,3) :
            sampleName += sampleElement[random.randint(0,n)]
        sample = {'name':sampleName}

        for target in tList :
            f = codecs.open(target + ".txt", 'r', 'utf-8')
            lines = f.readlines()
            keyList = []
            for line in lines:
                frags = line.split(":")
                keyList.append(frags[0])
            selection = keyList[random.randint(0, len(keyList)-1)]
            sample[target] = selection
        sampleList.append(sample)
    
    file = pathlib.Path("Samples.json")
    file.write_text(list_to_json(sampleList,data_to_json),encoding='utf-8')

if __name__ == "__main__":
    main()