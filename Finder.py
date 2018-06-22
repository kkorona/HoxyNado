# -*- coding: utf-8 -*-
import pymysql
import json
import pathlib
from pprint import pprint

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
    file = pathlib.Path('Samples.json')
    file_text = file.read_text(encoding='utf-8')
    json_data = json.loads(file_text)

    categoryList = ["sex", "name", "year", "major", "subway", "place", "class"]

    try:
        conn = pymysql.connect(host='localhost', user='root',
        password='high1uck', db='user_info', charset='utf8')
        added = {}
        curs = conn.cursor(pymysql.cursors.DictCursor)
        ret = []
        for category_i in categoryList:
            sql = "select * from maintbl where " + category_i + "=%s"
            user_value = json_data[category_i]
            curs.execute(sql, [user_value])

            rows = curs.fetchall()
            for row in rows:
                flag = True
                for category_j in categoryList:
                    if (row[category_j] is not None) and (row[category_j] is not user_value):
                        flag = False
                    elif row[category_j] is 'X':
                        flag = True
                if flag and not row['aid'] in added:
                    ret.append(row)
                    added[row['aid']] = 1
    
    finally:
        print(ret)
        file = pathlib.Path("Articles.json")
        file.write_text(list_to_json(ret,data_to_json),encoding='utf-8')
    
if __name__ == '__main__':
    main()