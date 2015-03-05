from bs4 import BeautifulSoup, Comment
import requests
import re

req = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')

html = req.content
soup = BeautifulSoup(html)

comments = soup.findAll(text=lambda text: isinstance(text, Comment))

s = comments[0]

n = ''

m = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', s)
# print(m)

for ans in m:
    ans = ans[1:]
    ans = ans[:len(ans)-1]
    # print(ans)
    small = ans[3]
    n += small

print('Answer -> ', n)
