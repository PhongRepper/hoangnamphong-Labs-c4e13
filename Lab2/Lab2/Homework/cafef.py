# 0. Dowload
from urllib.request import urlopen
from bs4 import BeautifulSoup

website = urlopen("http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn")
html_content = website.read().decode('UTF-8')
website.close()

soup = BeautifulSoup(html_content, 'html.parser', )

table_news = soup.find('table',id ='tableContent')
tr_new = table_news.find_all('tr')
# print(table_news.prettify())
print(tr_new)

for tr in tr_new:
    td_new = tr.find_all('td')
    for td in td_new:
        content = td.string
        print(content)
