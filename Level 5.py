import pickle
import urllib.request
import os

url = "http://www.pythonchallenge.com/pc/def/banner.p"
destination_filename = "banner.p"

urllib.request.urlretrieve(url, destination_filename)

pkl_file = open(destination_filename, 'rb')

data = pickle.load(pkl_file)

for d in data:
    s = ''
    for i in d:
        x, y = i
        for q in range(0, y):
            s += x
    print(s)

pkl_file.close()
os.remove(destination_filename)
