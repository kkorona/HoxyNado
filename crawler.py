# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import codecs
import requests


def main():
    cookies = {'guidance_sun_d41d8cd98f00b204e9800998ecf8427e': 'true'}
    ff = codecs.open("getArticle.txt", 'w', 'utf-8')
    ff.close()
    ff = codecs.open("getArticle.txt", 'a', 'utf-8')
    result = ""
    for i in range(1, 100, 1):
        url = "http://mypnu.net/index.php?mid=sun&page="+str(i)
        print(url)
        req = requests.get(url, cookies=cookies)
        html = req.text
        bs = BeautifulSoup(html, 'html.parser')
        l = bs.find_all('a', 'hx')
        v = bs.find_all('td', 'm_no')
        vv = []
        for view in v:
            vv.append(view.get_text())
        vv[0:4] = []
        for m, view in zip(l, vv):
            articleTitle = m.get_text().strip()
            articleURL = m.get('href')
            aidIndex = articleURL.find('document_srl=') + 13
            aid = articleURL[aidIndex:]

            aReq = requests.get(articleURL, cookies=cookies)
            html2 = aReq.text
            aBs = BeautifulSoup(html2, 'html.parser')
            articleDate = aBs.find('span', 'date m_no')
            ll = aBs.find('div', 'document_' + aid + '_0 xe_content')
            articleView = view
            if articleDate is None:
                continue
            articleDate = articleDate.get_text()
            articleTxt = ll.get_text()
            articleView = view
            print(articleTitle)
            print(articleDate)
            print(aid)

            result = ("- " + aid + " -\n" + articleTitle + "\n" +
                      articleDate + "\n" + articleView + "\n" +
                      articleTxt + "\n--------------" +
                      "----------------\n")
            ff.write(result)
    ff.close()

if __name__ == "__main__":
    main()
