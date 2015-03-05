from bs4 import BeautifulSoup, Comment
import requests

req = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')

html = req.content
soup = BeautifulSoup(html)

comments = soup.findAll(text=lambda text: isinstance(text, Comment))

s = comments[1]

n = ''

for l in s:
    if (s.count(l)) == 1:
        # print(l)
        n += l
        print(n)
print('Answer -> ', n)
