from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen("http://nhaczingmp3.com/bang-xep-hang/bai-hat-Viet-Nam/IWZ9Z08I.html")
html_content = website.read().decode("utf-8")
website.close()

soup = BeautifulSoup(html_content, "html.parser")

ul_news = soup.find('ul', 'box-song')
li_news = ul_news.find_all('li')

stt = 1
print("Bảng Xếp Hạng Bài Hát Việt Nam")
for li in li_news:
    # stt = len(li)
    a_detail = li.h3.a
    content = a_detail.string
    print(stt, content, sep='.')
    # print('-' * 20)
    stt += 1
# ul_news = div_news.find('ul')
# print(ul_news)
# # li_new_list = ul_news.find_all('li')

# ul_news = soup.find('ul')
# li_news_list = ul_news.find_all("li")
#
# for li in li_news_list:
#     a_detail = li.div
#     content = a_detail.string
#
