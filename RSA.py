
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


m=5

print("平文：", end = '')
print(m)
print("暗号化：", end='')
res = Encryption(101,19,13,m)
print(res)
print("復号化：",end='')
print(Decryption(101,19,13,res))



