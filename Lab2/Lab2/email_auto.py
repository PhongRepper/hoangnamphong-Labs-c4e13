from gmail import *
from random import choice

gmail = GMail("phongrepper@gmail.com", "repper1002")

file_names = ["1.html", "2.html", "3.html"]
file_name = choice(file_names)
# encoding='UTF-8' để không bị lỗi khi gõ dấu
# đọc file
template_file= open(file_name, encoding='UTF-8')
html_content = template_file.read()
template_file.close()
reasons = ["thich", "ghet", "luoi", "chiu"]
reason = choice(reasons)
# render reason
html_content = html_content.replace('{{reason}}', reason)
# send
msg = Message("Test Message", to ="C4e13.lab.huynq@gmail.com",
        text ="hello", html= html_content)

gmail.send(msg)
