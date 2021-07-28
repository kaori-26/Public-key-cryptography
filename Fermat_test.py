import math
import random
import time

S=1
max_num = 100000
#カーマイケル数
l = [561,1105,1729,2465,2821,6601,8911,10585,15841,29341,41041,46657,52633,62745,63973,75361]
prime = list()



def felmat_test(p):
	for i in range(1,S+1):
		a = random.randint(1,p-1)
		#print(a,end = ' ')
		b = pow(a,p-1,p)
		#print(b)
		if b != 1:
			return False
		if i == S:
			#prime.append(p)
			return True

count = 0
start = time.time()
for i in range(2,int(max_num)):
	if felmat_test(i) == 1 and i not in l:
		count += 1
end = time.time()
print("最大繰り返し回数：",S)
print(max_num, "までの素数の合計：",count)
print("所要時間：",end-start)