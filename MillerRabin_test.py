import math
import random
import time

S=3
#カーマイケル数
l = [561,1105,1729,2465,2821,6601,8911,10585,15841,29341,41041,46657,52633,62745,63973,75361]
def miller_rabin(p):

    if p == 2:
        return True
    if p%2 == 0:
        return False

    #kを先に求める
    v = (p-1)//2
    while v%2 == 0:
        v //= 2
    u = int(math.log(((p-1)/v),2))
    
    for i in range(1,S+1):       
        a = random.randint(2,p-1)        
        b = pow(a,v,p)

        if pow(a,p-1,p) != 1:
            return False
        
        j = 0
        while j<u and b!=1 and b!=p-1:
            b=pow(b,2,p)
            j+=1

        if (j == u or (j>0 and b==1)):
            return False
        if i == S:
            return True



count=0

print("最大繰り返し回数：",S)
for i in l:
    if miller_rabin(i) != 0:
        count+=1
print("カーマイケル数の誤判定個数：",count)

"""
print("最大繰り返し回数：",S)
start = time.time()
for i in range(2,10000000):
    if miller_rabin(i) != 0:
        count+=1
end = time.time()
print("1000000までの素数の合計：",count)
print("所要時間：",end-start)
"""


