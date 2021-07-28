import random
import math
S=100
def felmat_test(p):
	for i in range(1,S+1):
		a = random.randint(1,p-1)
		#print(a,end = ' ')
		b = pow(a,p-1,p)
		#print(b)
		if b != 1:
			return False
		if (i == S):
			return True

def modinv(a, m):
    b = m
    u = 1
    v = 0
    while (b):
        t = a // b
        a -= t * b
        a,b=b,a
        u -= t * v
        u,v=v,u
    u %= m
    if u < 0:
    	u += m
    return u

def Encryption(p,q,e,m):
	N=p*q
	#暗号文
	C=pow(m,e,N)
	return C

def Decryption(p,q,e,C):
	#秘密鍵
	d=modinv(e,(p-1)*(q-1))
	N=p*q
	m=pow(C,d,N)
	return m


#生成したい素数の長さn
n=10
#最大繰り返し回数
K=100
p_list = list()
for k in range(2):
	for j in range(1,K+1):
		bit_p = list()
		p=0
		for i in range(n-1):
			bit_p.append(random.randint(0,1))
		#print(bit_p)
		bit_p.append(1)
		#print(bit_p)
		for i in range(n):
			p+=pow(2,i)*bit_p[i]
		#print(p)
		if felmat_test(p) == True and p%3 != 1:
			p_list.append(p)
			break

print(p_list)#2つの素数
m=input()
print("平文：", end = '')
print(m)
print("暗号化：", end='')
res = Encryption(p_list[0],p_list[1],3,int(m))
print(res)
print("復号化：",end='')
print(Decryption(p_list[0],p_list[1],3,res))


