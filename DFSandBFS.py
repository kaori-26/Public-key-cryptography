def next(Cx,Cy):
	if (maze[Cx+1][Cy] == "0") and CL.count((Cx+1)*1000+Cy) == 0:
		#print("右")
		OL.append((Cx+1)*1000+Cy)
		#CL.append((Cx+1)*1000+Cy)
		#幅優先探索の時に使う
	if (maze[Cx][Cy+1] == "0") and CL.count(Cx*1000+(Cy+1)) == 0:
		#print("下")
		OL.append(Cx*1000+(Cy+1))
		#CL.append(Cx*1000+(Cy+1))
		#幅優先探索の時に使う
	if (maze[Cx-1][Cy] == "0") and CL.count((Cx-1)*1000+Cy) == 0:
		#print("左")
		OL.append((Cx-1)*1000+Cy)
		#CL.append((Cx-1)*1000+Cy)
		#幅優先探索の時に使う
	if (maze[Cx][Cy-1] == "0") and CL.count(Cx*1000+(Cy-1)) == 0:
		#print("上")
		OL.append(Cx*1000+(Cy-1))
		#CL.append(Cx*1000+(Cy-1))
		#幅優先探索の時に使う

f = open("/Users/otakaori/Doc/3_1_ex/1st/map1010","r")
MAP=f.read()
print(MAP)
#課題1

maze = MAP.splitlines()#迷路データを改行で区切る

#スタートのx,y座標
Sx=1
Sy=1
#ゴールのx,y座標
Gx=9
Gy=9
#現在のx,y座標、スタートに初期化
Cx=Sx
Cy=Sy
#オープンリスト
OL = list()
#クローズドリスト
CL = list()
#経路の出力時に使う
route = list()

#課題2のテスト用
print("(1,1)の時のオープンリスト")
next(1,1)
print(OL)
OL = list()
print("(9,9)の時のオープンリスト")
next(9,9)
print(OL)
OL = list()
print("(1,1)が探索済みの場合の(2,1)の時のオープンリスト")
CL.append(1*1000+(1))
next(2,1)
print(OL)


#dfs  <start>
while 1:
	CL.append(Cx*1000+Cy)
	next(Cx,Cy)
	if not CL or not OL:
		print("not found")
		break
	a = OL.pop()
	Cx = int(a/1000)
	Cy = int(a%1000)
	if Cx == Gx and Cy == Gy:
		break
	route.append((Cy,Cx))
	#print(Cy,Cx)
print(route)
#dfs  <end>

#bfs  <start>
CL.append(Cx*1000+Cy)
while 1:
	next(Cx,Cy)
	if not CL or not OL:
		print("not found")
		break
	a = OL.pop(0)
	Cx = int(a/1000)
	Cy = int(a%1000)
	if Cx == Gx and Cy == Gy:
		break
	route.append((Cy,Cx))
	#print(Cy,Cx)
print(route)
#bfs  <end>