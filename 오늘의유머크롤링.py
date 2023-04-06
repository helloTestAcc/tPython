# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
#특정한주제를 검색

import re 


#웹봇으로 크롤링을 금지
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}


#파일에 저장

#기존 파일 추가(append, read, write : a+)
f= open(r"c:\work\todayHumor.txt","a+",encoding="utf-8")
# f= open(r"c:\work\todayHumor.txt","wt",encoding="utf-8")
for n in range(1,11):
        #클리앙의 중고장터 주소 
        data ='https://www.todayHumor.co.kr/board/list.php?' \
        + 'table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
#        list = soup.findAll('a', attrs={'class':'list_subject'})
        list = soup.findAll('td', attrs={'class':'subject'})


# <td class="subject">
# <a href="/board/view.php?table=humordata&amp;no=1982982&amp;s_no=15393532&amp;kind=total&amp;page=1" target="_top">이게 사람이야 고라니야 </a><span class="list_memo_count_span"> [3]</span>  <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> </span><img src="http://www.todayhumor.co.kr/board/images/list_icon_shovel.gif?2" alt="펌글" style="margin-right:3px;top:2px;position:relative"> </td>


        for item in list:
                try:
                        # #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        # title = span2.text 
                        title=item.find('a').text.strip()
                        print(title)
                        # if (re.search('아이폰', title)):
                        #         print(title.strip())
                        #         print('https://www.clien.net'  + item['href'])
                        
                        # title = item.text
                        if (re.search('한국', title)):
                                 print(title.strip())
                                 f.write(title.strip()+"\n")
                        # print(title.strip())

                except:
                        pass
f.close() 
