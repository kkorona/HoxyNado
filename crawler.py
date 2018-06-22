# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import codecs
import requests
import Distributor


def main():
    cookies = {'guidance_sun_d41d8cd98f00b204e9800998ecf8427e': 'true'}
    ff = codecs.open("getArticle.txt", 'w', 'utf-8') # getArticle.txt파일을 열고 내용을 비워 깨끗한 파일로 만든다
    ff.close() # 깨끗한 파일이 된 getArticle.txt파일을 닫는다. 
    ff = codecs.open("getArticle.txt", 'a', 'utf-8') # getArticle.txt파일에 크롤링한 값을 저장하기 위해 open한다
    result = ""
    for i in range(1, 20, 1): # 총 19회  크롤링 예정
        url = "http://mypnu.net/index.php?mid=sun&page="+str(i) # 크롤링 할 사이트 주소이며 str(i)는 해당 게시판의 페이지를 의미한다
        print(url) # 실행 시 크롤링하는 URL 주소 출력한다.
        req = requests.get(url, cookies=cookies)
        html = req.text
        bs = BeautifulSoup(html, 'html.parser')
        l = bs.find_all('a', 'hx') # (약간 헷갈림) 게시판에서 글의 제목을 포함하고 있는 HTML 태그는 <a class = "hx"> 이다.
        v = bs.find_all('td', 'm_no') # (헷갈림) 게시판에서 글의 조회수를 포함하고 있는 HTML 태그는 <td class = "m_no"> 이다.
        vv = []
        for view in v:
            vv.append(view.get_text())
        vv[0:4] = []
        for m, view in zip(l, vv):
            articleTitle = m.get_text().strip() #게시물의 제목
            articleURL = m.get('href') # 게시물의 URL
            aidIndex = articleURL.find('document_srl=') + 13
            aid = articleURL[aidIndex:]

            aReq = requests.get(articleURL, cookies=cookies)
            html2 = aReq.text
            aBs = BeautifulSoup(html2, 'html.parser')
            articleDate = aBs.find('span', 'date m_no') # 게시물 작성 날짜 및 시간
            ll = aBs.find('div', 'document_' + aid + '_0 xe_content') #게시판에서 글의 내용을 포함하고 있는 HTML 태그는 <div class=”document_$id_0 xe_content”> 이다. 
            articleView = view
            if articleDate is None:
                continue
            articleDate = articleDate.get_text() #게시물 작성 날짜 및 시간
            articleTxt = ll.get_text() # 게시물의 글 내용
            articleView = view

            result = ("- " + aid + " -\n" + articleTitle + "\n" +   # 크롤링한 데이터들을 result로 묶었다.
                      articleDate + "\n" + articleView + "\n" +     
                      articleTxt + "\n--------------" +                                     
                      "----------------\n")
            ff.write(result) # getArticle에 result를 저장한다. 
            Distributor.add(aid, articleTitle, articleDate, articleTxt) # getArticle.txt에 저장한 크롤링한 데이터를 분류처리 모듈로 보낸다.
    ff.close() # 사용한 파일을 닫아 준다.

if __name__ == "__main__":
    main()
