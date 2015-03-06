# http://www.pythonchallenge.com/pc/return/bull.html

# Answer this?
# len(a[30])


# a = [1,       # 1(1) 1-1, 2-0
#    11,        # 2(2) 1-2, 2-0
#    21,        # 3(2) 1-1, 2-1
#    1211,      # 5(4) 1-3, 2-1
#    111221     # 8(6) 1-4, 2-2
#   ]

def look_and_say(number):
    result = ""

    repeat = number[0]
    number = number[1:]+" "
    times = 1

    for n in number:
        if n != repeat:
            result += str(times)+repeat
            times = 1
            repeat = n
        else:
            times += 1

    return result

num = "1"
a = [num]
for i in range(30):
    num = look_and_say(num)
    a.append(num)


print(len(a[30]))
