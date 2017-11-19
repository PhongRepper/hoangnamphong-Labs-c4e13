from urllib.request import urlopen
from bs4 import BeautifulSoup
# byte/binary
# 1.Dowload html content
website = urlopen("http://dantri.com.vn/")
html_content = website.read().decode('UTF-8')
website.close()

# 2.create BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
# nên đặt tên thẻ giống biến
ul_news = soup.find('ul', "ul1 ulnew")
li_news_list = ul_news.find_all("li")

for li in li_news_list:
    a_detail = li.h4.a
    title = a_detail['title'] #LẤy attribute
    content = a_detail.string #lấy content/string/value
    print(content)
    print("-" * 20)
# print (ul_news.prettify())
