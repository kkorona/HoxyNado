# -*- coding: utf-8 -*-
import pymysql
import json
import pathlib
from pprint import pprint

def data_to_json(data) :
    if type(data) is str : 
        return '"' + data + '"' 
    elif type(data) is list : 
        return list_to_json(data, data_to_json) 
    elif type(data) is int or type(data) is float : 
        return data.__str__() 
    elif type(data) is dict : 
        return dict_to_json(data, data_to_json) 
    else :
        return '""'

def list_to_json(list, func):
    out_str = "[" 
    for val in list:
        out_str += func(val)
        out_str += ", "

    if len(out_str) > 2:
        out_str = out_str[:-2]

    out_str += "]" 
    return out_str

def dict_to_json(dict, func) :
    out_str = "{"
    for key in dict.keys() :
        out_str += ('"' + key.__str__() + '"') 
        out_str += ": " 
        out_str += func(dict[key])
        out_str += ", " 
    if len(out_str) > 2:
        out_str = out_str[:-2]

    out_str += "}" 
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
