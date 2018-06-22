# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import codecs
import requests
import Distributor


def main():
    cookies = {'guidance_sun_d41d8cd98f00b204e9800998ecf8427e': 'true'}
    # 마이피누 반짝이 게시판 최초 입장 시 경고문이 뜨는데 이로인해 크롤링이 잘못되는 경우를 방지 하기 위하여 cookie로 추가되는 값을 true로 하기위하여 입력
    ff = codecs.open("getArticle.txt", 'w', 'utf-8') # getArticle.txt파일을 만들거나 혹은 동일 파일명이 있을 시 기존 내용을 지우기 위하여 w 로 열었다 닫는다.
    ff.close() # 빈 파일이 된 getArticle.txt파일을 닫는다. 
    ff = codecs.open("getArticle.txt", 'a', 'utf-8') # getArticle.txt파일에 크롤링한 값을 저장하기 위해 open한다
    result = "" # result 변수 생성한다.
    for i in range(1, 20, 1): # 총 19회  크롤링 예정
        url = "http://mypnu.net/index.php?mid=sun&page="+str(i) # 크롤링 할 사이트 주소이며 str(i)는 해당 게시판의 페이지를 의미한다
        print(url) # 실행 시 크롤링하는 URL 주소 출력한다.
        req = requests.get(url, cookies=cookies) # 해당 url에서 html 코드를 가져온다
        html = req.text # 가져온 html코드를 text로 변경
        bs = BeautifulSoup(html, 'html.parser') # 
        l = bs.find_all('a', 'hx') # 게시판에서 글의 제목을 포함하고 있는 HTML 태그는 <a class = "hx"> 이다.
        v = bs.find_all('td', 'm_no') # 게시판에서 글의 조회수를 포함하고 있는 HTML 태그는 <td class = "m_no"> 이다.
        vv = []
        for view in v:
            vv.append(view.get_text())
        vv[0:4] = []
        for m, view in zip(l, vv):
            articleTitle = m.get_text().strip() #게시물의 제목
            articleURL = m.get('href') # 게시물의 URL
            aidIndex = articleURL.find('document_srl=') + 13 
            aid = articleURL[aidIndex:]   # URL 에서 document_srl= 다음이 실제 게시글 id이므로 +13을 하였다.

            aReq = requests.get(articleURL, cookies=cookies) #해당 url에서 html 코드를 가져온다
            html2 = aReq.text # 가져온 html 코드를 text로 변경
            aBs = BeautifulSoup(html2, 'html.parser')
            articleDate = aBs.find('span', 'date m_no') # 게시물 작성 날짜 및 시간
            ll = aBs.find('div', 'document_' + aid + '_0 xe_content')
            #게시판에서 글의 내용을 포함하고 있는 HTML 태그는 <div class=”document_$id_0 xe_content”> 이다. 
            articleView = view
            if articleDate is None:
                continue
            articleDate = articleDate.get_text() # 게시물 작성 날짜 및 시간
            articleTxt = ll.get_text() # 게시물의 글 내용
            articleView = view 

            result = ("- " + aid + " -\n" + articleTitle + "\n" +   
                      articleDate + "\n" + articleView + "\n" +     
                      articleTxt + "\n--------------" +                                     
                      "----------------\n") # 크롤링한 데이터들을 result로 묶었다.
            ff.write(result) # getArticle에 result를 저장한다. 
            Distributor.add(aid, articleTitle, articleDate, articleTxt)
            # getArticle.txt에 저장한 크롤링한 데이터를 분류처리 모듈로 보낸다.
    ff.close() # 사용한 파일을 닫아 준다.

if __name__ == "__main__":
    main()
