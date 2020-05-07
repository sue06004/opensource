import pgzrun

WIDTH = 700
HEIGHT = 600
color = 1  # color 1은 노란색 2는 빨간색 0은 하얀색
gamestate = -1 # -1은 게임 시작 전 0은 게임 진행 중 1은 게임이 끝난 상태
tilestate = [
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0]
]
tileheight= [5,5,5,5,5,5,5]
color_state =1
cnt = 0 # 같은 색깔이 연속된 횟수

def draw():
	global gamestate
	if gamestate == -1:
		drawO()
		gamestate += 1
	else:
		return
def drawO():
	screen.clear()
	screen.fill((0,0,255))
	for h in range(0,6):
		for w in range(0,7):
			if tilestate[h][w] == 0:
				screen.draw.filled_circle((50+100*w, 50+100*h), 35, 'white')
			elif tilestate[h][w] == 1:
				screen.draw.filled_circle((50+100*w, 50+100*h), 35, 'yellow')
			else:
				screen.draw.filled_circle((50+100*w, 50+100*h), 35, 'red')

def on_mouse_down(pos,button):
	global color, gamestate
	if button == mouse.WHEEL_UP or button == mouse.WHEEL_DOWN: return
	if gamestate == 1:
		return 
	W = pos[0] // 100
	H = tileheight[W]
	tilestate[H][W] = color
	if H !=0:
		tileheight[W] -= 1
	if color == 1: color = 2
	else: color = 1
	drawO()
	gamestate = check4(H,W)


def check_win(list_color):
	global color_state, cnt
	if list_color == color_state and list_color != 0:
		cnt += 1
		if cnt >= 4:
			if color_state == 1:
				screen.draw.text("Yellow win", (300,300),color = 'green')
				return 1
			elif color_state == 2:
				screen.draw.text("Red win", (300,300),color = 'green')
				return 1
	else:
		color_state = list_color
		cnt = 1

def check4(h,w):
	global color_state, cnt
	#가로 체크
	color_state = 1
	cnt= 0
	for i in range(0,7):
		list_color = tilestate[h][i]
		if check_win(list_color) == 1: return 1
	
	# 세로 체크	
	color_state = 1
	cnt = 0
	for j in range(0,6):
		list_color = tilestate[j][w]
		if check_win(list_color) == 1: return 1
	
	# 대각선 체크(왼쪽아래에서 오른쪽위로)
	start_x = 0	 # 대각선의 왼쪽인덱스(시작부분)
	start_y = 0
	if h+w <=5:
		start_x = 0
		start_y = h+w
	else:
		start_x = h+w-5
		start_y = 5
	k = 0
	color_state = 1
	cnt = 0
	while True:
		if start_y-k < 0 or start_x+k > 6: break
		list_color = tilestate[start_y-k][start_x+k]
		if check_win(list_color) == 1: return 1
		k += 1
	
	# 대각선 체크(왼쪽위에서 오른쪽아래)
	if w-h >= 1:
		start_x = w-h
		start_y = 0
	else:
		start_x = 0
		start_y = h-w

	color_state = 1
	cnt = 0
	k = 0
	while True:
		if start_y+k > 5 or start_x+k > 6: break
		list_color = tilestate[start_y+k][start_x+k]
		if check_win(list_color) == 1: return 1
		k += 1
	
	return 0 # 4개가 연결이 아니면 0을 리턴

pgzrun.go()