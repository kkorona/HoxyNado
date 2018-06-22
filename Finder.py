# -*- coding: utf-8 -*-
import pymysql
import json
import pathlib
from pprint import pprint

# line 10-45의 JSON Converting Function은 다음 블로그의 글을 참조하여 작성하였습니다.
# https://blessingdev.wordpress.com/2017/11/03/term-project-python%EC%9C%BC%EB%A1%9C-json-%ED%8C%8C%EC%9D%BC%EC%9D%84-%EC%9D%BD%EA%B3%A0-%EC%93%B0%EA%B8%B0/

def data_to_json(data) :
    if type(data) is str : # string을 json 형식으로 변환
        return '"' + data + '"' 
    elif type(data) is list : # list를 json 형식으로 변환
        return list_to_json(data, data_to_json) # list 내의 원소들에 대해서 data_to_json을 재귀적으로 사용
    elif type(data) is int or type(data) is float : #수치 자료형을 json 형식으로 변환
        return data.__str__()
    elif type(data) is dict : # dict를 json 형식으로 변환
        return dict_to_json(data, data_to_json) # dict 내의 원소들에 대해서 data_to_json을 재귀적으로 사용
    else :
        return '""' # null data

def list_to_json(list, func):
    out_str = "[" # JSON list 시작
    for val in list:
        out_str += func(val)
        out_str += ", " # 원소 구분자 추가

    if len(out_str) > 2:
        out_str = out_str[:-2] # ]를 추가하기 위해서 마지막에 추가된 쉼표(,)와 공백( )을 제거

    out_str += "]" # JSON list 끝
    return out_str

def dict_to_json(dict, func) :
    out_str = "{" # JSON dict 시작
    for key in dict.keys() :
        out_str += ('"' + key.__str__() + '"') # 키값을 str형으로 변환하여 JSON dict key로 변환
        out_str += ": " 
        out_str += func(dict[key])
        out_str += ", " # 원소 구분자 추가
    if len(out_str) > 2:
        out_str = out_str[:-2] # }를 추가하기 위해서 마지막에 추가된 쉼표(,) 와 공백( )을 제거

    out_str += "}" # JSON dict 끝
    return out_str

def main():
    # pathlib module로 file을 read함. 한글을 포함하는 문서이므로 utf-8로 인코딩되어있음에 유의해서 읽어옴
    file = pathlib.Path('C:\\Users\\illak\\eclipse-workspace\\HoxyNado\\WebContent\\UserInfo.json')
    file_text = file.read_text(encoding='utf-8')
    json_data = json.loads(file_text)

    # 탐색을 실행할 특성들을 배열에 저장
    categoryList = ["sex", "name", "year", "major", "subway", "place", "class"]

    try:
        conn = pymysql.connect(host='localhost', user='root',
        password='high1uck', db='user_info', charset='utf8')
        added = {}
        curs = conn.cursor(pymysql.cursors.DictCursor)
        ret = []

        # conn : MySQL DB의 연결을 확인하는 객체
        # added : 게시글의 중복 카운팅을 피하기 위한 dict 객체
        # curs : MySQL cursor
        # ret : JSON으로 변환할 문서 내역

        for category_i in categoryList:
            sql = "select * from maintbl where " + category_i + "=%s"
            user_value = json_data[category_i]
            curs.execute(sql, [user_value])
            # user가 입력한 해당 category 특성을 가지고 있는 모든 값을 불러옴

            rows = curs.fetchall()
            for row in rows:
                if not row['aid'] in added: #중복검사
                    ret.append(row)
                    added[row['aid']] = 1
    
    finally:
        # 게시글을 JSON Array 형식으로 저장
        file = pathlib.Path("C:\\Users\\illak\\eclipse-workspace\\HoxyNado\\WebContent\\Articles.json")
        file.write_text("{\"Articles\" : " + list_to_json(ret,data_to_json) + "}",encoding='utf-8')
    
if __name__ == '__main__':
    main()