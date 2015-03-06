# http://www.pythonchallenge.com/pc/return/bull.html

# Answer this?
# len(a[30])

	                       
# a = [1, 		# 1(1) 1-1, 2-0
# 	 11,		# 2(2) 1-2, 2-0
# 	 21, 		# 3(2) 1-1, 2-1
# 	 1211, 		# 5(4) 1-3, 2-1
# 	 111221 	# 8(6) 1-4, 2-2
# 	]


def add_list(l):
	total = 0
	for q in l:
		total += int(q)
	return total


def Fib(n):
    if n == 0: 
    	return 0
    elif n == 1: 
    	return 1
    else: 
    	return Fib(n-1)+Fib(n-2)

fib_nums = [1]

num_list = []

a = []

for i in range(2,30):
	fib = Fib(i)
	print(str(i-2) + ' ' + str(fib))
	fib_nums.append(fib)
	if i > 3:
		num_of_twos = fib_nums[i-4]
		for n in range(0,num_of_twos):
			num_list.append(2)

	while add_list(num_list) < fib:
		num_list.append(1)
	# print(num_list)
	s = ''
	for o in num_list:
		s += str(o)
	a.append(s)
	num_list = []

# print(F(1)) 
# print(a)
