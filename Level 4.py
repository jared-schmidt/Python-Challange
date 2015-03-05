import requests


def url(nothing_num):
    return 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % nothing_num

num = '12345'
for x in range(0, 400):
    req = requests.get(url(num))
    nothing = req.content
    if ('yes' in str(nothing).lower()):
        print("Almost there...")
        # print("DIVIDED!")
        # print("DIVED NUM -> ", num)
        num = int(num)/2
    elif ('.html' in str(nothing).lower()):
        print("END")
        print(str(nothing))
        break
    else:
        num = ''
        # print(nothing)
        nothing = str(nothing)
        nothing = nothing[nothing.find("next nothing is"):]
        # print(nothing)

        for n in str(nothing):
            if n.isdigit():
                num += str(n)
